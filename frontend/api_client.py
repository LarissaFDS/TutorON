import os
import httpx
from typing import Optional, Dict, Any

# Configuração centralizada da URL do backend, permitindo sobrescrita via variável de ambiente.
BACKEND_URL = os.getenv("TUTORON_BACKEND_URL", "http://localhost:8000")

class APICommunicationError(Exception):
    """Exceção lançada quando ocorre um erro de rede, timeout ou o servidor está fora do ar."""
    pass

class APIValidationError(Exception):
    """Exceção lançada quando o backend rejeita o payload (Erro 422)."""
    pass

class AIServiceError(Exception):
    """Exceção lançada quando o serviço de IA falha no backend (Erro 502)."""
    pass

class InternalServerError(Exception):
    """Exceção lançada quando ocorre um erro inesperado no backend (Erro 500)."""
    pass

def send_student_question(question_text: str, context_text: Optional[str] = None) -> Dict[str, Any]:
    """
    Envia a dúvida do estudante para o endpoint de perguntas do backend do TutorOn.

    Args:
        question_text (str): Texto da dúvida acadêmica inserida pelo estudante.
        context_text (str | None): Código ou contexto adicional (opcional).

    Returns:
        dict: Dados estruturados retornados pelo backend contendo a chave 'answer'.

    Raises:
        APIValidationError: Se a pergunta for inválida (Erro 422).
        AIServiceError: Se a IA falhar ao processar a dúvida (Erro 502).
        InternalServerError: Se ocorrer um erro interno no servidor (Erro 500).
        APICommunicationError: Se houver recusa de conexão, timeout ou resposta não-JSON.
    """
    endpoint = f"{BACKEND_URL}/api/v1/questions"
    
    # Montagem do payload seguindo rigorosamente o contrato esperado pelo backend
    payload = {
        "question": question_text,
        "context": context_text
    }

    try:
        # Requisição isolada da interface, com timeout de 30 segundos (IA pode demorar um pouco)
        response = httpx.post(endpoint, json=payload, timeout=30.0)
        
        # Tratamento de erros HTTP baseados nos contratos definidos
        if response.status_code == 422:
            raise APIValidationError("A pergunta enviada é inválida ou está vazia.")
        
        if response.status_code == 502:
            raise AIServiceError("O serviço de IA falhou ao processar a requisição.")
            
        if response.status_code == 500:
            raise InternalServerError("Ocorreu um erro interno no backend.")
            
        # Levanta erro genérico HTTP para outros status de falha não mapeados
        response.raise_for_status()
        
        return response.json()

    except httpx.ConnectError:
        raise APICommunicationError(f"Conexão recusada. O backend está rodando em {BACKEND_URL}?")
    except httpx.TimeoutException:
        raise APICommunicationError("O servidor demorou muito para responder (Timeout).")
    except ValueError:
        raise APICommunicationError("A resposta do servidor não é um JSON válido.")
    except httpx.RequestError as e:
        raise APICommunicationError(f"Erro inesperado de rede: {str(e)}")
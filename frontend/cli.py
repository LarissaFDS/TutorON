import sys
from typing import Optional
from api_client import (
    send_student_question, 
    APICommunicationError, 
    APIValidationError, 
    AIServiceError, 
    InternalServerError
)

def display_header() -> None:
    """
    Exibe o cabeçalho principal da interface CLI do TutorOn.
    
    Args:
        Nenhum.
        
    Returns:
        None.
    """
    print("\n========================================")
    print("              TutorOn AI")
    print("         Seu tutor acadêmico")
    print("========================================\n")

def prompt_student_question() -> str:
    """
    Solicita a dúvida do usuário iterativamente até que uma entrada válida seja fornecida.
    Realiza a validação local (evita strings vazias) antes de enviar à API.

    Args:
        Nenhum.

    Returns:
        str: A dúvida do estudante, garantidamente não vazia.
    """
    while True:
        question = input("Digite sua dúvida:\n> ").strip()
        if question:
            return question
        print("[Aviso] A pergunta não pode estar vazia. Tente novamente.\n")

def prompt_optional_context() -> str | None:
    """
    Solicita código ou contexto adicional opcional ao estudante.

    O usuário pode pressionar Enter imediatamente para pular essa etapa.
    Caso forneça conteúdo, múltiplas linhas são aceitas até que uma linha vazia
    seja informada.

    Returns:
        str | None: O contexto fornecido pelo estudante ou None quando nenhum
        contexto foi informado.
    """
    print("\nDigite código ou contexto adicional (opcional, pressione Enter para pular):")
    
    lines = []
    while True:
        line = input("> ")
        
        if not lines and not line.strip():
            return None
            
        if lines and not line.strip():
            break
            
        lines.append(line)
        
    context = "\n".join(lines).rstrip()
    return context if context else None

def display_ai_response(response_data: dict) -> None:
    """
    Exibe a resposta formatada da Inteligência Artificial.
    Lê a chave 'answer' do payload de sucesso do backend e, opcionalmente, 
    mostra a origem ('source') como informação complementar de depuração.

    Args:
        response_data (dict): Dicionário retornado pela chamada HTTP de sucesso.

    Returns:
        None.
    """
    answer = response_data.get("answer", "Nenhuma resposta encontrada no payload.")
    source = response_data.get("source", "desconhecido")
    
    print("\n========================================")
    print("          Resposta do TutorOn")
    print("========================================\n")
    print(answer)
    print("\n========================================")
    print(f"[Fonte da resposta: {source}]")
    print("========================================\n")

def display_api_error(error_message: str) -> None:
    """
    Exibe mensagens de erro de forma amigável para o usuário, 
    evitando exibir rastros de execução (tracebacks) assustadores.

    Args:
        error_message (str): A mensagem de erro tratada a ser exibida.

    Returns:
        None.
    """
    print("\n[ERRO DO SISTEMA]")
    print(error_message)
    print("========================================\n")

def run_cli() -> None:
    """
    Função principal que orquestra o fluxo do Frontend CLI:
    1. Mostra a interface.
    2. Coleta inputs (pergunta e contexto).
    3. Chama a API via api_client.
    4. Exibe o resultado ou captura e trata erros técnicos para exibi-los amigavelmente.
    
    Args:
        Nenhum.
        
    Returns:
        None.
    """
    display_header()
    
    try:
        # 1. Coleta de dados com validação local básica
        question = prompt_student_question()
        context = prompt_optional_context()
        
        print("\nProcessando sua dúvida...")
        
        # 2. Requisição HTTP encapsulada
        response_data = send_student_question(question_text=question, context_text=context)
        
        # 3. Exibição do sucesso
        display_ai_response(response_data)
        
    except APIValidationError as e:
        display_api_error(f"Validação: {str(e)}")
    except AIServiceError:
        display_api_error("Não foi possível processar sua dúvida pela IA. Tente novamente.")
    except InternalServerError:
        display_api_error("Erro interno do servidor. Nossa equipe já foi notificada. Tente mais tarde.")
    except APICommunicationError as e:
        display_api_error(f"Falha de comunicação: {str(e)}\n\nVerifique se o backend está executando com:\n'uvicorn backend.main:app --reload'")
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário. Até logo!")
        sys.exit(0)
    except Exception as e:
        # Tratamento de último recurso (catch-all) para evitar quebra grosseira do terminal
        display_api_error(f"Um erro inesperado e desconhecido ocorreu: {str(e)}")

if __name__ == "__main__":
    # Garante a execução da CLI apenas se o arquivo for chamado diretamente.
    run_cli()
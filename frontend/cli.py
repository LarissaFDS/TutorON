import sys
from api_client import (
    send_student_question, 
    APICommunicationError, 
    APIValidationError, 
    AIServiceError, 
    InternalServerError
)

RULE = "-" * 60

def display_header() -> None:
    """
    Exibe o cabeçalho principal da interface CLI do TutorON.
    
    Args:
        Nenhum.
        
    Returns:
        None.
    """
    print()
    print("TutorON · monitoria de Projeto e Análise de Algoritmos")
    print("Escreva sua dúvida. Se ela envolver código ou pseudocódigo, cole na etapa seguinte.")
    print(RULE)

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
        print("Escreva a dúvida antes de continuar.\n")

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
    print("\nCódigo ou contexto adicional (opcional). Termine com uma linha vazia; Enter direto pula:")
    
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
    
    print()
    print(RULE)
    print(answer)
    print(RULE)
    print(f"Gerada por: {source}. Confira com o material da disciplina antes de usar na prova.")
    print()

def display_api_error(error_message: str) -> None:
    """
    Exibe mensagens de erro de forma amigável para o usuário, 
    evitando exibir rastros de execução (tracebacks) assustadores.

    Args:
        error_message (str): A mensagem de erro tratada a ser exibida.

    Returns:
        None.
    """
    print()
    print(f"Não foi possível responder. {error_message}")
    print()

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
        
        print("\nConsultando o tutor. Pode levar até dois minutos...")
        
        # 2. Requisição HTTP encapsulada
        response_data = send_student_question(question_text=question, context_text=context)
        
        # 3. Exibição do sucesso
        display_ai_response(response_data)
        
    except APIValidationError as e:
        display_api_error(str(e))
    except AIServiceError:
        display_api_error("O serviço de IA falhou ou está indisponível. Tente de novo em instantes.")
    except InternalServerError:
        display_api_error("O backend teve um erro interno. Veja o log do uvicorn para o detalhe.")
    except APICommunicationError as e:
        display_api_error(f"Falha de comunicação: {str(e)}\n\nVerifique se o backend está executando com:\n'uvicorn backend.main:app --reload'")
    except KeyboardInterrupt:
        print("\n\nCancelado.")
        sys.exit(0)
    except Exception as e:
        # Tratamento de último recurso (catch-all) para evitar quebra grosseira do terminal
        display_api_error(f"Erro inesperado: {str(e)}")

if __name__ == "__main__":
    # Garante a execução da CLI apenas se o arquivo for chamado diretamente.
    run_cli()
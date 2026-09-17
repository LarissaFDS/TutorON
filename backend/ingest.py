import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pypdf import PdfReader
from supabase import create_client


load_dotenv()


# ---------------------------------------------------------
# Clientes
# ---------------------------------------------------------

gemini = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)


PDF_PATH = "materials/disciplina.pdf"


# ---------------------------------------------------------
# Embedding
# ---------------------------------------------------------

def generate_embedding(text: str) -> list[float]:

    response = gemini.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
            output_dimensionality=1536,
        ),
    )

    return response.embeddings[0].values


# ---------------------------------------------------------
# Ingestão
# ---------------------------------------------------------

def main():

    print("Lendo PDF...")

    reader = PdfReader(PDF_PATH)

    # Criar registro do documento
    document_response = supabase.table(
        "documents"
    ).insert({
        "name": os.path.basename(PDF_PATH)
    }).execute()

    document_id = document_response.data[0]["id"]

    print(
        f"Documento criado: {document_id}"
    )

    # Processar páginas
    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        text = page.extract_text()

        if not text or not text.strip():
            print(
                f"Página {page_number}: sem texto"
            )
            continue

        text = text.strip()

        print(
            f"Processando página {page_number}..."
        )

        embedding = generate_embedding(text)

        supabase.table(
            "chunks"
        ).insert({
            "document_id": document_id,
            "content": text,
            "page_number": page_number,
            "embedding": embedding,
        }).execute()

    print()
    print("Ingestão concluída!")


if __name__ == "__main__":
    main()
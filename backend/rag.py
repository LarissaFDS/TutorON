import os

import ollama

from dotenv import load_dotenv
from supabase import create_client


load_dotenv()


# ---------------------------------------------------------
# Clientes
# ---------------------------------------------------------

EMBEDDING_MODEL = "bge-m3"

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)


# ---------------------------------------------------------
# Embeddings
# ---------------------------------------------------------

def generate_embedding(text: str) -> list[float]:

    response = ollama.embeddings(
        model=EMBEDDING_MODEL,
        prompt=text,
    )

    return response["embedding"]


# ---------------------------------------------------------
# Busca no Supabase
# ---------------------------------------------------------

def search_context(
    question: str,
    limit: int = 3
) -> list[dict]:

    # Embedding da pergunta
    embedding = generate_embedding(question)

    # Busca os chunks semanticamente mais próximos
    response = supabase.rpc(
        "match_chunks",
        {
            "query_embedding": embedding,
            "match_count": limit,
        },
    ).execute()

    return response.data
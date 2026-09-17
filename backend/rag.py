import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
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


# ---------------------------------------------------------
# Embeddings
# ---------------------------------------------------------

def generate_embedding(
    text: str,
    task_type: str
) -> list[float]:

    response = gemini.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(
            task_type=task_type,
            output_dimensionality=1536,
        ),
    )

    return response.embeddings[0].values


# ---------------------------------------------------------
# Busca no Supabase
# ---------------------------------------------------------

def search_context(
    question: str,
    limit: int = 3
) -> list[dict]:

    # Embedding da pergunta
    embedding = generate_embedding(
        question,
        "RETRIEVAL_QUERY"
    )

    # Busca os chunks semanticamente mais próximos
    response = supabase.rpc(
        "match_chunks",
        {
            "query_embedding": embedding,
            "match_count": limit,
        },
    ).execute()

    return response.data
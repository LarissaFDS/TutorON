import os
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=False)

def main():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    print("KEY configurada:", bool(key))

    if not url or not key:
        raise RuntimeError(
            "SUPABASE_URL e SUPABASE_KEY precisam estar configuradas no ambiente"
        )

    supabase = create_client(url, key)

    response = supabase.table("documents").select("*").limit(1).execute()

    print("Supabase OK!")
    print("Documents returned:", len(response.data))


if __name__ == "__main__":
    main()

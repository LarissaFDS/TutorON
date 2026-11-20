# TutorON hospedado (Render, Hugging Face Spaces ou qualquer serviço com Docker).
# O modelo local NÃO roda aqui: ele fica no PC da equipe e entra via worker (docs/HOSPEDAGEM.md).
FROM python:3.11-slim

# Bibliotecas do sistema para as animações (Manim: cairo/pango) e fontes com acento.
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential pkg-config libcairo2-dev libpango1.0-dev ffmpeg fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Sem dados de alunos na imagem: tudo vai para o Supabase. dados/ aqui é só cache temporário.
RUN mkdir -p dados && useradd --create-home tutoron && chown -R tutoron /app/dados
USER tutoron

ENV PYTHONUNBUFFERED=1 PORT=8000
EXPOSE 8000
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port ${PORT} --proxy-headers --forwarded-allow-ips='*'"]

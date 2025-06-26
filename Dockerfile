FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

RUN mkdir -p /app/output

# 🟨 TEMPORARILY COMMENT OUT MAIN.PY (we run it manually for now)
# CMD ["sh", "-c", "python main.py && cd output && python3 -m http.server 8080"]

# ✅ JUST SERVE OUTPUT FOLDER
CMD ["python3", "-m", "http.server", "8080", "--directory", "output"]

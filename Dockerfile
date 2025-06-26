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

ENV PATH="/opt/venv/bin:$PATH"

# ✅ Run main.py and then serve output
CMD ["sh", "-c", "python main.py && cd output && python3 -m http.server 8080"]

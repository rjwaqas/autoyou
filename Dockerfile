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

RUN mkdir -p /app/output /app/static

ENV PATH="/opt/venv/bin:$PATH"

# Run main script + Flask
CMD ["sh", "-c", "python main.py && cp output/output.mp4 static/output.mp4 && python serve_video.py"]

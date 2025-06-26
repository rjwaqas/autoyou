# 👇 START WITH A PYTHON BASE IMAGE
FROM python:3.12-slim

# Install system dependencies needed for Pillow and MoviePy
RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your files
COPY . .

# Install Python dependencies
RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Activate virtual environment on container start
ENV PATH="/opt/venv/bin:$PATH"

# Run the app
CMD ["python", "main.py"]

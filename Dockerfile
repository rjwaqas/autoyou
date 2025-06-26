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

# Set working directory inside container
WORKDIR /app

# Copy all local files into container
COPY . .

# Install Python dependencies
RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# ✅ Create output folder to store final video
RUN mkdir -p /app/output

# Activate the virtual environment on start
ENV PATH="/opt/venv/bin:$PATH"

# Run the main script
CMD ["python", "serve_video.py"]

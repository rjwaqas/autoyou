# 👇 START WITH A PYTHON BASE IMAGE
FROM python:3.12-slim

# Install system dependencies for Pillow, MoviePy, and Flask
RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Create output directory
RUN mkdir -p /app/output

# Expose port for Flask
EXPOSE 8080

# Activate virtual environment and run app
ENV PATH="/opt/venv/bin:$PATH"
CMD ["sh", "-c", "python main.py && python serve_video.py"]

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

# Create output folder
RUN mkdir -p /app/output

# Set environment path
ENV PATH="/opt/venv/bin:$PATH"

# Run the script and serve the output folder
CMD sh -c "python main.py && cd output && python3 -m http.server 8080"

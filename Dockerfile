# Use Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Copilot CLI
RUN apt-get update && apt-get install -y curl unzip

# Install GitHub Copilot CLI
RUN curl -fsSL https://github.com/github/copilot-cli/releases/latest/download/copilot-linux-amd64.tar.gz \
    | tar -xz -C /usr/local/bin

# Copy your FastAPI app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

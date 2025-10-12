FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl tar gzip

# Download GitHub Copilot CLI, extract and move to /usr/local/bin
RUN curl -sSL https://github.com/github/copilot-cli/releases/latest/download/copilot-linux-amd64.tar.gz \
    | tar -xz -C /usr/local/bin

# Make sure binary is executable
RUN chmod +x /usr/local/bin/copilot

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

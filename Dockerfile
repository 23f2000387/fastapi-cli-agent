FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl unzip

# Install GitHub Copilot CLI
RUN curl -sSL https://github.com/github/copilot-cli/releases/latest/download/copilot-linux-amd64.tar.gz | tar -xz -C /usr/local/bin

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

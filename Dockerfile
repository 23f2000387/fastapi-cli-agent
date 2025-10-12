FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y curl tar

# Create bin folder if not exists
RUN mkdir -p /usr/local/bin

# Download Copilot CLI and make it executable
RUN curl -fsSL https://github.com/github/copilot-cli/releases/latest/download/copilot-linux-amd64.tar.gz \
    | tar -xz -C /usr/local/bin \
    && chmod +x /usr/local/bin/copilot

# Copy your app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

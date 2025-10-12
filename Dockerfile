# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install GitHub Copilot CLI (example using npm)
RUN apt-get update && apt-get install -y curl nodejs npm \
    && npm install -g @github/copilot-cli

# Copy your app code
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

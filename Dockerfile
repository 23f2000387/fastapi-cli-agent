FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl git

# Install Node.js (required for Copilot CLI)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Install Copilot CLI globally
RUN npm install -g @github/copilot-cli

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

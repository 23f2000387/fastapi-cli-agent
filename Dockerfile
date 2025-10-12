# Use official Python base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy code
COPY main.py /app

# Install FastAPI + Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn

# Expose port for FastAPI
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

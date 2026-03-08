FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY ../scripts/ ./scripts/
COPY . ./api/

# Create directories
RUN mkdir -p /tmp/pptx-uploads /tmp/pptx-outputs

# Expose port
EXPOSE 8000

# Run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

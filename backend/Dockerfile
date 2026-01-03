FROM python:3.10-slim

WORKDIR /app

# Installeer de nodige bibliotheken
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Start de backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
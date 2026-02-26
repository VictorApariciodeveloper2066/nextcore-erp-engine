# Usamos una imagen ligera de Python
FROM python:3.11-slim

# Evita que Python genere archivos .pyc y permite logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalamos dependencias del sistema para PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc

# Instalamos dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el contenido de la carpeta actual (backend) al WORKDIR (/app)
COPY . .
FROM python:3.11-slim
WORKDIR /RETO2
COPY . .
CMD ["python", "notas.py"]
FROM python:3.10-slim

# Información del mantenedor
LABEL maintainer="ilanangelesrodriguez@gmail.com"
LABEL description="Analizador Kasiski para cifrados Vigenère - Curso de Seguridad Informática"
LABEL version="1.0.0"

# Directorio de trabajo
WORKDIR /app

# Copiar código de la aplicación
COPY . .

# Instalar dependencias
RUN pip install flask

# Crear usuario no-root para seguridad
#RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
#USER appuser

# Exponer puerto
EXPOSE 5000

# Variables de entorno
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Comando de inicio
CMD ["python", "app.py"]
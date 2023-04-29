# Utiliza la imagen oficial de Python como base
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos de la aplicación
COPY requirements.txt .

# Instala los paquetes necesarios
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copia el resto del código fuente de la aplicación
COPY . .

# Define el puerto que se expondrá
EXPOSE 5000

# Ejecuta el comando para iniciar la aplicación
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

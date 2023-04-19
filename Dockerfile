# Utiliza la imagen base de Python 3.8
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos e instala las dependencias
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 5001

# Ejecuta la aplicación
CMD ["python", "app.py"]

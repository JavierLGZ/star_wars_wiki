FROM python:3.10-slim-bullseye

# Establece las variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ACCEPT_EULA=Y

# Define el directorio de trabajo
WORKDIR /app

# Copia el contexto de la aplicacion en el directorio de trabajo.
# Excluye los archivos señalados en .dockerfile
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip \
    && pip install wheel \
    && pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

RUN chmod +x entrypoint.sh

CMD ["entrypoint.sh"]

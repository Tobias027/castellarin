FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . .

# Configura el entorno virtual
ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Crea el entorno virtual
RUN python3.11 -m venv $VIRTUAL_ENV

# Actualiza pip e instala las dependencias
RUN $VIRTUAL_ENV/bin/pip install --upgrade pip
RUN $VIRTUAL_ENV/bin/pip install --no-cache-dir -r requirements.txt

# Comando de inicio
CMD ["reflex", "run", "--env", "prod", "--backend-only"]


FROM python:3.12-slim

# 2. Instalar dependencias y crear usuario en una sola capa
RUN apt-get update && \
    apt-get install -y python3-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir flask && \
    addgroup --gid 1000 no-root && \
    adduser --uid 1000 --ingroup no-root --shell /bin/sh --disabled-password --gecos "" no-root

# 3. Copiar código y cambiar al usuario no-root
COPY . /app
WORKDIR /app
USER no-root

# 4. Exponer puerto y comando
EXPOSE 5000
CMD ["python", "app.py"]

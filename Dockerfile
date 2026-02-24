FROM python:3.12-alpine 

# Instalar dependencias y crear usuario en una sola capa
RUN apk add --no-cache python3-dev build-base && \
    pip install --no-cache-dir flask azure-identity azure-keyvault-secrets && \
    addgroup -g 1000 no-root && \
    adduser -u 1000 -G no-root -s /bin/sh -D no-root

# Copiar la aplicación y cambiar al usuario no-root
COPY . /app
WORKDIR /app
USER no-root

# Exponer puerto y comando
EXPOSE 5000
CMD ["python", "app.py"]

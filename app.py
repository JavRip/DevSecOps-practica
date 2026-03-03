from flask import Flask
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
import os

# Crear la aplicación Flask
app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Obtener variables de entorno (seguro)
        tenant_id = os.environ.get('AZURE_TENANT_ID')
        client_id = os.environ.get('AZURE_CLIENT_ID') 
        client_secret = os.environ.get('AZURE_CLIENT_SECRET')
        key_vault_name = os.environ.get('KEY_VAULT_NAME')
        secret_name = os.environ.get('SECRET_NAME', 'API-Key')
        
        # Validar que las variables existen
        if not all([tenant_id, client_id, client_secret, key_vault_name]):
            return "Error: Faltan variables de entorno de configuración", 500
        
        # Usar ClientSecretCredential con variables de entorno (seguro)
        credential = ClientSecretCredential(
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret
        )
        
        # Construir URI del Key Vault
        key_vault_uri = f"https://{key_vault_name}.vault.azure.net/"
        
        # Crear cliente de Key Vault
        client = SecretClient(vault_url=key_vault_uri, credential=credential)
        
        # Obtener el secreto
        secret = client.get_secret(secret_name)
        secret_value = secret.value
        
        return f"¡Hola! App segura con Azure Key Vault. Secret obtenido: {secret_value[:10]}..."
    
    except Exception as e:
        return f"Error al acceder al Key Vault: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración del Key Vault
KEY_VAULT_NAME = "kv-devsecops1" 
KEY_VAULT_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net/"
SECRET_NAME = "API-Key"

@app.route('/')
def home():
    try:
        credential = DefaultAzureCredential()
        
        # Crear cliente de Key Vault
        client = SecretClient(vault_url=KEY_VAULT_URI, credential=credential)
        
        # Obtener el secreto
        secret = client.get_secret(SECRET_NAME)
        secret_value = secret.value
        
        return f"¡Hola! App segura con Azure Key Vault. Secret obtenido: {secret_value[:10]}..."
    
    except Exception as e:
        return f"Error al acceder al Key Vault: {str(e)}"

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    # Escuchar en todas las interfaces (0.0.0.0) y puerto 5000
    app.run(host='0.0.0.0', port=5000)

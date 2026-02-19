from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Endpoint principal - responde a peticiones GET a /
@app.route('/')
def home():
    return "¡Hola! Esta es mi aplicación Docker segura para la práctica de DevSecOps."

# Punto de entrada para ejecutar la aplicación
if __name__ == '__main__':
    # Escuchar en todas las interfaces (0.0.0.0) y puerto 5000
    app.run(host='0.0.0.0', port=5000)

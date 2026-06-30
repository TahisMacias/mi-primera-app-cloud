from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Primera App Cloud - Britany</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body { font-family: sans-serif; background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); height: 100vh; display: flex; justify-content: center; align-items: center; color: #fff; }
            .card { background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2); padding: 3rem; border-radius: 20px; text-align: center; max-width: 500px; width: 90%; }
            h1 { font-size: 2.2rem; margin-bottom: 1rem; }
            p { font-size: 1.1rem; color: #e0e0e0; margin-bottom: 2rem; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>¡CI/CD desde GitHub Funcionando al 100%! 🚀🔥</h1>
            <p>Esta aplicación fue desplegada con éxito por <strong>Britany</strong> usando CI/CD.</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()

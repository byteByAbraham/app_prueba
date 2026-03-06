from flask import Flask, render_template_string, request
import time

app = Flask(__name__)

users = []

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Portal de Apoyo Estudiantil</title>
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            text-align: center; 
            background-color: #eef2f7; 
            padding: 50px; 
            margin: 0;
        }
        .container { 
            background: white; 
            padding: 40px; 
            border-radius: 15px; 
            box-shadow: 0px 10px 25px rgba(0,0,0,0.1); 
            display: inline-block; 
            max-width: 400px;
        }
        h1 { color: #333; margin-bottom: 10px; }
        p { color: #666; margin-bottom: 25px; }
        input { 
            margin: 8px 0; 
            padding: 12px; 
            width: 90%; 
            border-radius: 8px; 
            border: 1px solid #ddd; 
            font-size: 16px;
        }
        button { 
            margin-top: 15px;
            padding: 12px 25px; 
            background-color: #28a745; 
            color: white; 
            border: none; 
            border-radius: 8px; 
            font-size: 16px;
            font-weight: bold;
            cursor: pointer; 
            width: 100%;
            transition: background 0.3s;
        }
        button:hover { background-color: #218838; }
        .success-msg { 
            margin-top: 20px;
            padding: 10px;
            background-color: #d4edda;
            color: #155724;
            border-radius: 5px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Portal de Apoyo Estudiantil</h1>
        <p>Regístrate para recibir ayuda con tus proyectos de ingeniería.</p>
        <form method="POST">
            <input type="text" name="name" placeholder="Nombre Completo" required><br>
            <input type="email" name="email" placeholder="Correo Electrónico" required><br>
            <button type="submit">Registrarme Ahora</button>
        </form>
        {% if msg %} 
            <div class="success-msg">{{ msg }}</div> 
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    time.sleep(0.5)
    msg = None
    if request.method == 'POST':
        name = request.form.get('name')
        users.append(name) 
        msg = f"¡Gracias, {name}! Te has registrado con éxito."
    return render_template_string(HTML_PAGE, msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=False)
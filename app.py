from flask import Flask, render_template_string, request

app = Flask(__name__)

users = []

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Soporte Técnico - Registro</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; padding: 50px; }
        .container { background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); display: inline-block; }
        input { margin: 10px; padding: 10px; width: 200px; border-radius: 5px; border: 1px solid #ccc; }
        button { padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Student Support Portal</h1>
        <p>Please register to get help with your projects.</p>
        <form method="POST">
            <input type="text" name="name" placeholder="Full Name" required><br>
            <input type="email" name="email" placeholder="Email Address" required><br>
            <button type="submit">Register Now</button>
        </form>
        {% if msg %} <p style="color: green;">{{ msg }}</p> {% endif %}
    </div>
</body>
</html>
'''

import time

@app.route('/', methods=['GET', 'POST'])
def home():
    time.sleep(2)
    msg = None
    if request.method == 'POST':
        name = request.form.get('name')
        users.append(name) 
        msg = f"Thank you, {name}! You are registered."
    return render_template_string(HTML_PAGE, msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
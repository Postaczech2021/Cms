from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    models_path = os.path.join('food', 'models.py')
    return render_template('index.html', models_path=models_path)

if __name__ == '__main__':
    app.run(debug=True)

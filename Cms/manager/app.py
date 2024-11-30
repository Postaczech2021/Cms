from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='.')

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

@app.route('/')
def index():
    base_path = os.path.join(os.path.dirname(__file__), '../food')
    files_content = {
        'models.py': read_file(os.path.join(base_path, 'models.py')),
        'views.py': read_file(os.path.join(base_path, 'views.py')),
        'urls.py': read_file(os.path.join(base_path, 'urls.py')),
        'forms.py': read_file(os.path.join(base_path, 'forms.py'))
    }
    return render_template('index.html', files_content=files_content)

@app.route('/save', methods=['POST'])
def save():
    base_path = os.path.join(os.path.dirname(__file__), '../food')
    filename = request.form['filename']
    content = request.form['content']
    file_path = os.path.join(base_path, filename)
    write_file(file_path, content)
    return index()

@app.route('/style.js')
def style_js():
    return send_from_directory(os.path.dirname(__file__), 'style.js')

if __name__ == '__main__':
    app.run(debug=True)

import numpy as np
from flask import Flask, request, jsonify, render_template
from datetime import date
import pickle

UPLOAD_FOLDER = 'D/COVID19/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/upload', methods=['GET', 'POST'])
def upload():
   if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
        
@app.route('/show/<filename>')
def uploaded_file(filename):
    filename = 'http://127.0.0.1:5000/publish/' + filename
    return render_template('template.html', filename=filename)

@app.route('/publish/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    if 'profile_image' not in request.files:
        return "No File Uploaded"

    file = request.files['profile_image']

    if file.filename == '':
        return "No Selected File"

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(filepath)

    return render_template(
        'result.html',
        image_path=filepath
    )

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
from service import prediction
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def hello_world():

    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    _, file_extension = os.path.splitext(file.filename)

    allowed_extensions = {'.jpg', '.jpeg', '.png'}
    if file_extension.lower() not in allowed_extensions:
        return 'Invalid file format'

    if file:
        image_bytes = file.read()
        result = prediction(image_bytes)
        predic = {
            'prediction': "Parasitized" if result.tolist()[0][0] == 0 else "Uninfected"
        }
        return jsonify(predic)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)

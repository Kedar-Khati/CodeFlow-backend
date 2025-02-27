from flask import Flask, request, send_file
import os
from flask_cors import CORS  # Import CORS
from trial import generate_backend

app = Flask(__name__)
CORS(app)

@app.route('/generate-backend', methods=['POST'])
def generate_backend_endpoint():
    json_data = request.json
    zip_filename = generate_backend(json_data)
    return send_file(zip_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
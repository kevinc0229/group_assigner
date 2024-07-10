from flask import Flask, request, jsonify, send_from_directory
import pandas as pd

app = Flask(__name__,  static_folder='frontend')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    if file:
        df = pd.read_csv(file)
        # Call your processing function here
        processed_df = process_csv(df)
        return processed_df.to_json()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

def process_csv(df):
    return df

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
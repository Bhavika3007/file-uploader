from flask import Flask, request, render_template, jsonify
import boto3
import os

app = Flask(__name__)

# Load environment variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        filename = file.filename
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            filename,
            ExtraArgs={'ContentType': file.content_type}  # ACL removed
        )
        file_url = f"https://{BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{filename}"
        return jsonify({'url': file_url})
    except Exception as e:
        print("Error uploading file:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

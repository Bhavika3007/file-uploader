# Simple Flask File Uploader using AWS S3

## Objective
This project demonstrates a lightweight Flask web application to upload files directly to an AWS S3 bucket and return a public URL for each uploaded file. The project is designed for easy deployment and clean integration with cloud storage.

---

## Features
- Upload files directly via a simple HTML frontend.
- Store uploaded files securely in an AWS S3 bucket.
- Instantly return public URLs for uploaded files.
- Minimal and portable backend, ready for deployment.

---

## Folder Structure
file-uploader/
├─ app.py
├─ requirements.txt
├─ runtime.txt
├─ Procfile
├─ .gitignore
├─ README.md
└─ templates/
└─ index.html


---

## Setup Steps

1. **Clone the repository**
git clone https://github.com/<your-username>/file-uploader.git
cd file-uploader
### Create a virtual environment (optional but recommended)
python -m venv venv
### Activate it
venv\Scripts\activate   # Windows
### Install dependencies
pip install -r requirements.txt
### Create a .env file with your AWS credentials:

AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_REGION=<your-region>
S3_BUCKET_NAME=<your-bucket-name>
Run the app locally

python app.py
Open http://127.0.0.1:5000 in your browser.

---

## Deployment
Can be deployed on free hosting platforms like Render or Railway.

For deployment, set your AWS environment variables on the platform.

Example: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, S3_BUCKET_NAME.

---

## Reflection
Learned to integrate Flask with AWS S3 for file uploads.

Learned to return public URLs for uploaded files.

Built a simple backend ready for deployment with minimal dependencies.

---

## Tech Stack
Backend: Python, Flask

Frontend: HTML (templates/index.html)

Cloud Storage: AWS S3

Deployment: Can use Render, Railway, or other cloud platforms

yaml
Copy code

---

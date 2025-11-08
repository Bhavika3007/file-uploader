# Simple File Uploader

A lightweight **Flask backend** for uploading files to **AWS S3**, designed for easy deployment and demonstration of cloud integration.  
This project allows uploading files via a frontend, stores them securely in S3, and provides a public URL for each uploaded file.

---

## Objective

This project was built to:  
-> Create a simple backend for uploading files securely to AWS S3.  
-> Provide an easily deployable backend using Flask.  
-> Provide a deployed frontend link so that it can be accessed anywhere.  
-> Demonstrate full integration with AWS cloud storage.

---

## Features

-> Upload files directly from a frontend (HTML)  
-> Store uploaded files inside an AWS S3 bucket  
-> Get public URLs for uploaded files instantly  
-> Simple and portable — runs locally or on cloud hosting  
-> Minimal dependencies and easy to understand

---

## Folder Structure
---
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

## Step 1: Setting up the Project Repository

mkdir file-uploader
cd file-uploader

## Step 2: Configuring the Backend
Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   
### Install dependencies
pip install -r requirements.txt
### Create a .env file in the root folder with your AWS credentials:
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_REGION=<your-region>
S3_BUCKET_NAME=<your-bucket-name>

## Step 3: Running the Application Locally
python app.py
Open http://127.0.0.1:5000 in your browser to access the frontend.

## Step 4: Frontend
A simple HTML page (templates/index.html) allows users to select a file and upload it to the S3 bucket.

The app returns a public URL for the uploaded file.

## Step 5: Deployment
Can be deployed on free cloud hosting platforms such as Render or Railway.

Make sure to set AWS environment variables on the platform:
AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, S3_BUCKET_NAME.

## Tech Stack
-> Backend: Python, Flask
-> Frontend: HTML
-> File Uploads: Flask + Boto3
-> Cloud Services: AWS S3
-> Deployment: Local / Cloud Hosting Platforms (Render, Railway)

## Reflection of What I Have Learnt
-> Learned how to integrate Flask with AWS S3 for file uploads.
-> Learned to return public URLs for uploaded files.
-> Built a simple, deployable backend with minimal dependencies.


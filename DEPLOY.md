# Deploying Handwritten OCR to Google Cloud

This document provides instructions for deploying the Handwritten OCR application to Google Cloud Platform.

## Prerequisites

1. [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed
2. A Google Cloud account with billing enabled
3. [Docker](https://docs.docker.com/get-docker/) installed (for local testing)
4. Google Cloud project created (our current project ID: `lucid-diode-452919`)
5. Google Cloud Vision API enabled in your project

## Deployment Options

There are two main options for deploying this application to Google Cloud:

1. **Google Cloud Run** (recommended): For containerized applications with automatic scaling
2. **Google App Engine**: For web applications with standard scaling

## Option 1: Deploying to Google Cloud Run

### Manual Deployment Steps

1. **Authenticate with Google Cloud:**

   ```bash
   gcloud auth login
   ```

2. **Set your project ID:**

   ```bash
   gcloud config set project lucid-diode-452919
   ```

3. **Build and push the Docker image:**

   ```bash
   gcloud builds submit --tag gcr.io/lucid-diode-452919/handwritten-ocr
   ```

4. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy handwritten-ocr \
     --image gcr.io/lucid-diode-452919/handwritten-ocr \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars="SECRET_KEY=your-secure-secret-key" \
     --set-env-vars="GOOGLE_APPLICATION_CREDENTIALS=lucid-diode-452919-p1-e5138e5e4227.json"
   ```

### Using the Deployment Script

Alternatively, you can use the provided `deploy.sh` script:

1. Make the script executable:

   ```bash
   chmod +x deploy.sh
   ```

2. Run the script:
   ```bash
   ./deploy.sh
   ```

## Option 2: Deploying to Google App Engine

1. **Authenticate with Google Cloud:**

   ```bash
   gcloud auth login
   ```

2. **Set your project ID:**

   ```bash
   gcloud config set project lucid-diode-452919
   ```

3. **Deploy to App Engine:**

   ```bash
   gcloud app deploy app.yaml
   ```

4. **Open the deployed application:**
   ```bash
   gcloud app browse
   ```

## Environment Variables

Set these environment variables in your deployment:

- `SECRET_KEY`: A secure secret key for Flask sessions
- `GOOGLE_APPLICATION_CREDENTIALS`: Path to your Google Cloud credentials JSON file
- `GOOGLE_CLIENT_ID`: Your Google OAuth client ID (if using Google login)
- `EMAIL_SENDER`: Email address for sending notifications
- `EMAIL_PASSWORD`: Password for the sender email
- `EMAIL_RECIPIENT`: Recipient email for feedback

## Database Considerations

The application currently uses SQLite, which is not suitable for production in a cloud environment. For production, consider:

1. **Cloud SQL for SQLite replacement:**

   - Update `database.py` to use Cloud SQL
   - Use environment variables for database credentials

2. **Alternatives:**
   - Firestore for a serverless database option
   - Cloud Datastore for non-relational storage

## Cloud Storage

For storing uploaded images, consider using Google Cloud Storage instead of local file storage:

1. Enable the Google Cloud Storage API
2. Update the application code to use Cloud Storage for file uploads
3. Set appropriate permissions for the service account

## Monitoring and Logging

After deployment, set up:

1. **Cloud Monitoring** for application performance insights
2. **Cloud Logging** for centralized logging
3. **Error Reporting** for tracking application errors

## Continuous Deployment

For automated deployments:

1. Set up a GitHub repository
2. Configure Google Cloud Build triggers
3. Create a `cloudbuild.yaml` configuration file

## Security Considerations

1. Secure all API keys and credentials
2. Implement proper authentication and authorization
3. Set up Identity-Aware Proxy (IAP) if needed
4. Use Secret Manager for sensitive credentials

# Deploying Handwritten OCR to Render

This guide provides instructions for deploying the Handwritten OCR application to Render.

## Prerequisites

1. A Render account (sign up at [render.com](https://render.com))
2. Your code in a Git repository (GitHub, GitLab, or Bitbucket)

## Deployment Steps

### Method 1: Direct from GitHub

1. **Log in to your Render Dashboard**

   - Go to [dashboard.render.com](https://dashboard.render.com)

2. **Create a New Web Service**

   - Click on "New" button in the top right
   - Select "Web Service"

3. **Connect your repository**

   - Connect to your GitHub/GitLab/Bitbucket account if not already connected
   - Select the repository containing your Handwritten OCR application

4. **Configure the service**

   - Name: `handwritten-ocr` (or your preferred name)
   - Environment: `Python 3`
   - Region: Choose the region closest to your users
   - Branch: `main` (or your default branch)
   - Build Command: `./build.sh`
   - Start Command: `gunicorn app:app`

5. **Configure Environment Variables**

   - Scroll down to the "Environment" section
   - Add the following environment variables:
     - `SECRET_KEY`: Generate a secure random string
     - `GOOGLE_APPLICATION_CREDENTIALS`: If using Google Vision API

6. **Set up Persistent Disk**

   - In the "Advanced" section, add a persistent disk
   - Mount Path: `/app/static/uploads`
   - Size: 1 GB (or more if needed)

7. **Deploy the service**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

### Method 2: Using Render Blueprint (render.yaml)

1. **Ensure your repository has a render.yaml file**

   - The file is already created in this repository

2. **Log in to your Render Dashboard**

   - Go to [dashboard.render.com](https://dashboard.render.com)

3. **Create a new Blueprint instance**

   - Click on "New" button
   - Select "Blueprint"
   - Connect to your repository

4. **Deploy the Blueprint**
   - Render will automatically detect the render.yaml file
   - Review the services to be created
   - Click "Apply" to deploy

## After Deployment

1. **Verify the application is running**

   - Render will provide a URL for your application (e.g., `https://handwritten-ocr.onrender.com`)
   - Visit the URL to ensure the application is working properly

2. **Set up Google Vision API credentials**

   - In the Render dashboard, navigate to your web service
   - Go to the "Environment" tab
   - If you're using Google Vision API, you need to add your credentials:
     - Either upload your JSON key file to the service
     - Or set the appropriate environment variables

3. **Monitor your application**
   - Use the Render dashboard to monitor logs, metrics, and performance

## Troubleshooting

- **Application fails to build**

  - Check the build logs for errors
  - Ensure all required dependencies are in `requirements.txt`

- **Application crashes on startup**

  - Check the logs for runtime errors
  - Verify that environment variables are set correctly

- **Database issues**

  - Ensure the persistent disk is configured correctly
  - Check file permissions for the database file

- **Vision API not working**
  - Verify your Google Cloud credentials are correctly set up
  - Check that the Vision API is enabled in your Google Cloud project

## Scaling and Maintenance

- **Auto-scaling**

  - By default, Render will automatically scale your service based on traffic
  - You can configure scaling settings in the service dashboard

- **Updates and Deployments**

  - Push changes to your repository
  - Render will automatically rebuild and deploy your application

- **Backups**
  - Regularly backup your database and uploaded files
  - Consider implementing a backup strategy for your persistent data

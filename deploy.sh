#!/bin/bash
# Google Cloud Platform deployment script

# Set variables (change these as needed)
PROJECT_ID="lucid-diode-452919"
SERVICE_NAME="handwritten-ocr"
REGION="us-central1"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting deployment to Google Cloud...${NC}"

# Authenticate with Google Cloud (uncomment if needed)
# echo -e "${YELLOW}Authenticating with Google Cloud...${NC}"
# gcloud auth login

# Set the project
echo -e "${YELLOW}Setting Google Cloud project to: $PROJECT_ID${NC}"
gcloud config set project $PROJECT_ID

# Build and push the container image
echo -e "${YELLOW}Building and pushing container image...${NC}"
gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME

# Deploy to Cloud Run
echo -e "${YELLOW}Deploying to Cloud Run...${NC}"
gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars="SECRET_KEY=your-secret-key-here" \
  --set-env-vars="GOOGLE_APPLICATION_CREDENTIALS=lucid-diode-452919-p1-e5138e5e4227.json"

echo -e "${GREEN}Deployment complete!${NC}"
echo -e "${GREEN}Your service should be available at:${NC}"
gcloud run services describe $SERVICE_NAME --platform managed --region $REGION --format="value(status.url)" 
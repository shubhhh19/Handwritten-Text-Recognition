#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Running initialization script..."
python init_app.py

echo "Build completed successfully!" 
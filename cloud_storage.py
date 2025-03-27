'''
    Filename: cloud_storage.py
    Project: Handwritten OCR | Capstone Project 2025
    Description: Helper functions for Google Cloud Storage operations
'''

import os
from google.cloud import storage
from werkzeug.utils import secure_filename
import tempfile

# Get GCS bucket name from environment variable or use default
BUCKET_NAME = os.environ.get('GCS_BUCKET_NAME', 'handwritten-ocr-files')

def get_storage_client():
    """Create and return a Google Cloud Storage client."""
    return storage.Client()

def upload_to_gcs(file, folder="uploads"):
    """
    Upload a file to Google Cloud Storage.
    
    Args:
        file: The file object from request.files
        folder: The folder within the bucket to store the file
        
    Returns:
        public_url: The public URL of the uploaded file
        local_path: The temporary local path where file was saved (for processing)
    """
    if not file:
        return None, None
        
    # Create a secure filename
    filename = secure_filename(file.filename)
    
    # Create a temporary file for local processing
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    file.save(temp_file.name)
    temp_file.close()
    
    # Get the storage client
    client = get_storage_client()
    
    # Get bucket
    try:
        bucket = client.get_bucket(BUCKET_NAME)
    except Exception as e:
        # If bucket doesn't exist, try to create it
        print(f"Bucket {BUCKET_NAME} doesn't exist. Creating it...")
        bucket = client.create_bucket(BUCKET_NAME)
    
    # Create GCS blob
    blob_name = f"{folder}/{filename}"
    blob = bucket.blob(blob_name)
    
    # Upload the file
    blob.upload_from_filename(temp_file.name)
    
    # Make the blob publicly accessible
    blob.make_public()
    
    return blob.public_url, temp_file.name

def delete_from_gcs(filename, folder="uploads"):
    """
    Delete a file from Google Cloud Storage.
    
    Args:
        filename: The name of the file to delete
        folder: The folder within the bucket where the file is stored
    """
    if not filename:
        return False
        
    # Get the storage client
    client = get_storage_client()
    
    try:
        # Get bucket
        bucket = client.get_bucket(BUCKET_NAME)
        
        # Create GCS blob
        blob_name = f"{folder}/{filename}"
        blob = bucket.blob(blob_name)
        
        # Delete the blob
        blob.delete()
        return True
    except Exception as e:
        print(f"Error deleting file from GCS: {e}")
        return False

def list_files_in_gcs(folder="uploads"):
    """
    List all files in a folder in Google Cloud Storage.
    
    Args:
        folder: The folder within the bucket to list files from
        
    Returns:
        A list of filenames in the folder
    """
    # Get the storage client
    client = get_storage_client()
    
    try:
        # Get bucket
        bucket = client.get_bucket(BUCKET_NAME)
        
        # List blobs in the folder
        blobs = bucket.list_blobs(prefix=folder)
        
        # Return the filenames
        return [blob.name.replace(f"{folder}/", "") for blob in blobs 
                if not blob.name.endswith('/')]
    except Exception as e:
        print(f"Error listing files from GCS: {e}")
        return [] 
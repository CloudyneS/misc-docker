#!/usr/bin/python3
import os
from azure.storage.blob import BlobClient

class Upload:
    sas_url: str = None
    upload_file: str = None
    destination_path: str = None
    client: BlobClient = None
    
    def __init__(self):
        try:
            self.sas_url = os.environ['AZURE_SAS_URL']
            self.upload_file = os.environ['UPLOAD_FILE']
            self.destination_path = os.environ['DESTINATION_PATH']
        except KeyError as e:
            raise Exception(f"Missing environment variable: {e}")
        
        print("Successfully set environment variables")
        self.client = BlobClient.from_blob_url(self.sas_url.replace("?", f"/{self.destination_path}?"))
        
        print("Successfully created client")
        self.upload_file()
        
        print("Successfully uploaded file")

    def upload_file(self):
        print("Started uploading file...")
        with open(self.upload_file, "rb") as data:
            self.client.upload_blob(data, overwrite=True, blob_type="BlockBlob")            

if __name__ == '__main__':
    print("Starting upload....")
    Upload()
import boto3
import logging
from botocore.exceptions import ClientError

def upload(filepath, filename):
	print("Uploading", filename, "...")
	try:
                s3 = boto3.resource('s3')
                bucket = "koreva-liubov-input-bucket"
                s3.meta.client.upload_file(filepath, bucket, filename)
	except ClientError as e:
		logging.error(e)
	print("Uploaded successfully.")

upload("mediafiles/Windsurfing.mov", "Windsurfing.mov")
upload("mediafiles/Llama_drama_1080p.mp4", "Llama_drama_1080p.mp4")
upload("mediafiles/Sample-DV.mxf", "Sample-DV.mxf")

print("Done.")

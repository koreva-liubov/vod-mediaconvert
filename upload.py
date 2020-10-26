import boto3
import logging
from botocore.exceptions import ClientError

def upload(filename):
	print("Uploading", filename, "...")
	try:
		s3 = boto3.resource('s3')
		bucket = "koreva-liubov-input-bucket"
		s3.meta.client.upload_file(filename, bucket, filename)
	except ClientError as e:
		logging.error(e)
	print("Uploaded successfully.")

upload("10-sec-windsurfing.mp4")
upload("10-sec-beach.mp4")
upload("10-sec-lid.mp4")

print("Done.")

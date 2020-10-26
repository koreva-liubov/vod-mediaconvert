# Video Conversion Workflow for MediaConvert
In this project Amazon S3 services and Lambda are used to monitor S3 watchfolder bucket and automatically trigger AWS MediaConvert jobs. An ingest workflow will be triggered to convert the video each time media file is uploaded to AWS S3 bucket. The lambda will send the video to the MediaConvert service to produce MP4 output with an specific graphic overlay on it.

## Project description

mediafiles/ - a number of various media files used for testing

lambda_function.py - Lambda fiunction written by using Boto3 AWS SDK for Python

mediaconvert-job.json - JSON file with transcoding job parameters

myVODLambda-5cacec2a-4a5a-4e6c-916e-5951ca0e139e.zip - Lambda deployment package containing lambda function and json file

myVODLambda.yml - YAML file for MediaConvert

upload.py - script used for testing the workflow

## Testing instructions

1. Run upload.py script in the terminal. You should have boto3 in your environment.
2. Go to http://koreva-liubov-input-bucket.s3-website-us-west-2.amazonaws.com/ to see the list of input media files
3. Once the job finished, the resulting output will be visible at: http://koreva-liubov-output-bucket.s3-website-us-west-2.amazonaws.com/
4. You can upload another sample files by modifying upload.py


import json
import boto3
import uuid
import os

def lambda_handler(event, context):

    # Lambda handler is triggered when media file is uploaded to S3 watchfolder bucket.

    # Get input video URL
    sourceS3Bucket = event['Records'][0]['s3']['bucket']['name']
    sourceS3Key = event['Records'][0]['s3']['object']['key']
    sourceS3 = 's3://' + sourceS3Bucket + '/' + sourceS3Key
    sourceS3Basename = os.path.splitext(os.path.basename(sourceS3))[0]

    # S3 output bucket destination 
    destinationS3 = 's3://koreva-liubov-output-bucket'
    destinationS3basename = os.path.splitext(os.path.basename(destinationS3))[0]

    # IAM permission for MediaConvert 
    mediaConvertRole = os.environ['MediaConvertRole']

    region = os.environ['AWS_DEFAULT_REGION']
    statusCode = 200
    
    try:
        # Request an account-specific mediaconvert endpoint for current region
        mediaconvert_endpoints = boto3.client('mediaconvert', region_name=region).describe_endpoints()

        # Add an account-specific endpoint to the client session 
        mediaconvert = boto3.client('mediaconvert', endpoint_url=mediaconvert_endpoints['Endpoints'][0]['Url'])

        # Read transcoding job settings from JSON file and store as Python object
        with open("mediaconvert-job.json", "r") as json_file:
            job_object = json.load(json_file)

        # Get job settings from job object
        job_settings = job_object['Settings']

        # Update job settings with the source video
        job_settings['Inputs'][0]['FileInput'] = sourceS3
    
        # Create the transcoding job
        job = mediaconvert.create_job(Role=mediaConvertRole, Settings=job_settings)
    
    except Exception as e:
        print ('Exception: %s' % e)
        statusCode = 500
        raise

    return {  
        'statusCode': statusCode,
        'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}
    }
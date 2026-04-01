import json
import base64
import boto3

# Connect to Rekognition
rekognition = boto3.client('rekognition', region_name='us-east-2')

def lambda_handler(event, context):
    try:
        # 1. Parse the image sent from your website
        body = json.loads(event.get('body', '{}'))
        image_remote = body.get('image', '')
        
        if not image_remote:
            return {'statusCode': 400, 'body': json.dumps({'error': 'No image provided'})}

        # 2. Convert base64 string to actual image bytes
        image_bytes = base64.b64decode(image_remote)

        # 3. Call Rekognition to detect emotions
        response = rekognition.detect_faces(
            Image={'Bytes': image_bytes},
            Attributes=['ALL']
        )

        # 4. Extract the most likely emotion
        detected_emotion = "Neutral"
        if response['FaceDetails']:
            emotions = response['FaceDetails'][0]['Emotions']
            # Sort by highest confidence
            emotions.sort(key=lambda x: x['Confidence'], reverse=True)
            detected_emotion = emotions[0]['Type']

        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*", # Required for S3 website to talk to Lambda
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            'body': json.dumps({'emotion': detected_emotion})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': 'Internal processing error'})}
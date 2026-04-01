import json
import urllib3

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    API_KEY = "789f8de0-0174-4d67-be12-b8fcce403283"
    
    # WORKING CONTEXT ID (Ann Therapist - RudiCare)
    MY_CONTEXT_ID = "1c05f397-bd80-4d06-a377-898776b10608" 
    
    payload = {
        "mode": "FULL",
        "avatar_id": "dd73ea75-1218-4ef3-92ce-606d5f7fbc0a",
        "interactivity_type": "CONVERSATIONAL",
        "avatar_persona": {
            "voice_id": "c2527536-6d1f-4412-a643-53a3497dada9",
            "context_id": MY_CONTEXT_ID 
        }
    }
    
    headers = {
        "X-API-KEY": API_KEY.strip(),
        "Content-Type": "application/json"
    }
    
    try:
        encoded_data = json.dumps(payload).encode('utf-8')
        response = http.request('POST', "https://api.liveavatar.com/v1/sessions/token", 
                                body=encoded_data, headers=headers, timeout=10.0)
        res_data = json.loads(response.data.decode('utf-8'))
        
        return {
            'statusCode': 200,
            'body': json.dumps(res_data.get('data', res_data))
        }
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}

import json
import urllib3

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    API_KEY = "789f8de0-0174-4d67-be12-b8fcce403283"
    
    # Check if the frontend is asking for credits specifically
    query_params = event.get('queryStringParameters', {})
    if query_params and query_params.get('action') == 'get_credits':
        try:
            url = "https://api.liveavatar.com/v1/users/credits"
            headers = {"X-API-KEY": API_KEY.strip(), "accept": "application/json"}
            response = http.request('GET', url, headers=headers)
            res_data = json.loads(response.data.decode('utf-8'))
            
            # Extract credits_left from the response
            credits = res_data.get('data', {}).get('credits_left', '0')
            return {
                'statusCode': 200,
                'body': json.dumps({"credits_left": credits})
            }
        except Exception as e:
            return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}

    # DEFAULT ACTION: Create Session Token (Your existing code)
    MY_CONTEXT_ID = "1c05f397-bd80-4d06-a377-898776b10608"
    MY_AVATAR_ID = "dd73ea75-1218-4ef3-92ce-606d5f7fbc0a"
    payload = {
        "mode": "FULL",
        "avatar_id": MY_AVATAR_ID,
        "interactivity_type": "CONVERSATIONAL",
        "avatar_persona": {"voice_id": "c2527536-6d1f-4412-a643-53a3497dada9", "context_id": MY_CONTEXT_ID}
    }
    
    try:
        url = "https://api.liveavatar.com/v1/sessions/token"
        headers = {"X-API-KEY": API_KEY.strip(), "Content-Type": "application/json"}
        response = http.request('POST', url, body=json.dumps(payload), headers=headers)
        res_data = json.loads(response.data.decode('utf-8'))
        token_data = res_data.get('data', {})
        
        return {
            'statusCode': 200,
            'body': json.dumps({"session_token": token_data.get('session_token'), "data": token_data})
        }
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}

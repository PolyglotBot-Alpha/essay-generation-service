import os
import requests


def call_tts_service(tts_service_url, text):
    service_url = tts_service_url + '/generate-speech'
    # Prepare the request data and headers
    payload = {'text': text}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    # Make a synchronous POST request
    try:
        response = requests.post(service_url, data=payload, headers=headers,
                                 timeout=120)  # 5-second timeout for the request
        if response.status_code == 200:
            response_data = response.json()
            if 'file_url' in response_data:
                return response_data['file_url']  # Return the URL of the uploaded audio file
            else:
                return {'error': 'Response does not contain file URL'}
        else:
            return {'error': 'Failed to generate or upload speech', 'status_code': response.status_code}
    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., connection errors, timeout)
        return {'error': str(e)}


print(call_tts_service('http://127.0.0.1:5000', "Hello World"))

import os
import requests

from CircuitBreaker import CircuitBreaker

# Global circuit breaker instance
tts_circuit_breaker = CircuitBreaker()


def call_tts_service(tts_service_url, text):
    service_url = tts_service_url + '/generate-speech'
    # Prepare the request data and headers
    payload = {'text': text}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    # Make a synchronous POST request
    try:
        response = requests.post(service_url, data=payload, headers=headers, timeout=120)  # Increased timeout
        if response.status_code == 200:
            response_data = response.json()
            if 'file_url' in response_data:
                tts_circuit_breaker.record_success()
                return response_data['file_url']  # Return the URL of the uploaded audio file
            else:
                tts_circuit_breaker.record_failure()
                return {'error': 'Response does not contain file URL'}
        else:
            tts_circuit_breaker.record_failure()
            return {'error': 'Failed to generate or upload speech', 'status_code': response.status_code}
    except requests.exceptions.RequestException as e:
        tts_circuit_breaker.record_failure()
        return {'error': str(e)}

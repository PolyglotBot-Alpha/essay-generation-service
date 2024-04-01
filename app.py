from flask import Flask, request, jsonify
from py_eureka_client import eureka_client
from dotenv import load_dotenv
import os
from gpt import OpenAIContentGenerator
from service import call_tts_service
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Eureka server URL
eureka_server = os.getenv('EUREKA_SERVER_URL')

# Application name, host, and port
app_name = "AI-Content-Generation"

# The port at which your Flask application will be accessible
port = int(os.getenv('PORT', 8080))

eureka_client.init(eureka_server=eureka_server,
                   app_name=app_name,
                   instance_port=port)


@app.route('/')
def hello_world():
    return 'Hello, World from Flask Eureka Client!'


@app.route('/generate_essay', methods=['POST'])
def process_input():
    # Extract input from the request
    user_input = request.json.get('user_input', '')

    api_key = os.getenv('API_KEY')

    if api_key is not None:
        content_generator = OpenAIContentGenerator(api_key)
        generated_essay = content_generator.gpt_generate_essay(user_input)

        tts_service_url = os.getenv("TTS_SERVER_URL")
        audio_url = call_tts_service(tts_service_url, generated_essay)

        return jsonify({"essay": generated_essay, "audio_url": audio_url}), 200
    else:
        return jsonify({"message": "API key not found. Please set the API_KEY environment variable."}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

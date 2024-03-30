from flask import Flask, request, jsonify
from py_eureka_client import eureka_client
from dotenv import load_dotenv
import os
from gpt import OpenAIContentGenerator

app = Flask(__name__)

# Eureka server URL
eureka_server = "http://localhost:8761/eureka/"

# Application name, host, and port
app_name = "AI-Content-Generation"

# The port at which your Flask application will be accessible
port = 6000

eureka_client.init(eureka_server=eureka_server,
                   app_name=app_name,
                   instance_port=port)

# Load environment variables from .env file
load_dotenv()


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
        return jsonify({"essay": generated_essay, "audio_url": ""}), 200
    else:
        return jsonify({"message": "API key not found. Please set the API_KEY environment variable."}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

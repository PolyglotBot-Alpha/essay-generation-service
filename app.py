from flask import Flask
from py_eureka_client import eureka_client
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Eureka server URL
eureka_server = "http://localhost:8761/eureka/"

# Application name, host, and port
app_name = "AI-Content-Generation"
app_host = "localhost"
app_port = 5000

# Load environment variables from .env file
load_dotenv()


@app.route('/')
def hello_world():
    return 'Hello, World from Flask Eureka Client!'


@app.route('/generate_essay')
def essay_generation():
    api_key = os.getenv('API_KEY')
    if api_key is not None:
        return api_key
    else:
        return "API key not found. Please set the API_KEY environment variable."


if __name__ == '__main__':
    # Register the application with Eureka
    eureka_client.init(eureka_server=eureka_server,
                       app_name=app_name,
                       instance_port=app_port,
                       instance_host=app_host)
    app.run(host=app_host, port=app_port)

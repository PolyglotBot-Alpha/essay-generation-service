from flask import Flask
from py_eureka_client import eureka_client

app = Flask(__name__)

# Eureka server URL
eureka_server = "http://localhost:8761/eureka/"

# Application name, host, and port
app_name = "flask-eureka-client"
app_host = "localhost"
app_port = 5000

@app.route('/')
def hello_world():
    return 'Hello, World from Flask Eureka Client!'

if __name__ == '__main__':
    # Register the application with Eureka
    eureka_client.init(eureka_server=eureka_server,
                       app_name=app_name,
                       instance_port=app_port,
                       instance_host=app_host)
    app.run(host=app_host, port=app_port)

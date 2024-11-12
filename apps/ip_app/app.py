from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def show_ip():
    local_ip = socket.gethostbyname(socket.gethostname())
    return f'Container IP: {local_ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
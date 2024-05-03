from flask import Flask, request, abort
import logging
import time
from threading import Thread

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Dictionary to store request counts for each IP address
ip_counts = {}

# Threshold for maximum requests per second from a single IP
threshold = 10000

# Cooldown period in seconds before bringing the server back up
cooldown_period = 60

# Function to check for potential DDoS attacks
def detect_ddos(ip):
    if ip in ip_counts:
        current_time = time.time()
        # Remove records older than 1 minute
        ip_counts[ip] = [t for t in ip_counts[ip] if current_time - t <= 60]
        if len(ip_counts[ip]) > threshold:
            logger.warning(f"Potential DDoS attack detected from {ip}!")
            # Cut connection from the IP address
            abort(403)
            # Wait for the cooldown period before bringing the server back up
            time.sleep(cooldown_period)
    else:
        ip_counts[ip] = []

def network_activity_scanner():
    # Implement your network activity scanner here
    # This function should establish a baseline of network activity
    # and monitor for any significant deviations
    pass

@app.route('/')
def index():
    ip = request.remote_addr
    detect_ddos(ip)
    logger.info(f"Incoming request from {ip}")
    ip_counts[ip].append(time.time())  # Record the timestamp of the request
    return """
    <html>
    <head>
    <style>
    body {
        background-color: black;
        color: blue;
        text-align: center;
    }
    </style>
    </head>
    <body>
    <h1>This is a test server for Greek Hackers!</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Greece.svg/2560px-Flag_of_Greece.svg.png" alt="Greek Flag" style="width: 200px; height: auto;">
    </body>
    </html>
    """

if __name__ == '__main__':
    # Start the network activity scanner in a separate thread
    scanner_thread = Thread(target=network_activity_scanner)
    scanner_thread.start()

    app.run(debug=True)


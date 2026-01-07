#!/usr/bin/python3
"""
Simple API Server using http.server module
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for our simple API
    """
    
    def do_GET(self):
        """
        Handle GET requests for different endpoints
        """
        # Root endpoint
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        # /data endpoint - returns JSON data
        elif self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        
        # /status endpoint - returns API status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        
        # /info endpoint (optional, but mentioned in expected output)
        elif self.path == '/info':
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info).encode())
        
        # Handle undefined endpoints - 404 Not Found
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run_server(port=8000):
    """
    Start the HTTP server on the specified port
    """
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on port {port}")
    print(f"Access the API at: http://localhost:{port}")
    print("Endpoints available:")
    print("  /         - Welcome message")
    print("  /data     - Sample JSON data")
    print("  /status   - API status")
    print("  /info     - API information")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")

if __name__ == '__main__':
    run_server()

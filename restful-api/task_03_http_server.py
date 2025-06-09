#!/usr/bin/python3
"""
This module creates a basic HTTP API using Python's built-in http.server module.

It provides simple endpoints:
- `/` returns a plain text welcome message
- `/data` returns a JSON object with sample user information
- `/status` returns a plain text OK message
- `/info` returns JSON-formatted metadata about the API
- Any other route returns a 404 error with a plain text message

The server is designed for learning purposes and demonstrates
how to handle GET requests and send different content types.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom request handler class for a basic HTTP API.

    This class handles GET requests for various endpoints,
    responding with JSON or plain text depending on the route.
    It uses standard HTTP response codes and content types.
    """

    def do_GET(self):
        """
        Handles HTTP GET requests.

        Supported endpoints:
        - `/` responds with a plain text welcome message.
        - `/data` responds with a JSON dictionary containing user data.
        - `/status` responds with a plain text "OK" message.
        - `/info` responds with API metadata in JSON format.
        - Any other route returns a 404 error with a plain text message.
        """
        if self.path == "/":

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data_response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data_response).encode("utf-8"))

        elif self.path == "/status":

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info_response = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info_response).encode("utf-8"))

        else:

            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    Starts the HTTP server on the specified port using the provided handler.

    Args:
        server_class: The class to use for the HTTP server (default: HTTPServer).
        handler_class: The class that handles incoming requests (default: SimpleAPIHandler).
        port: The port number to listen on (default: 8000).

    The server runs indefinitely until interrupted (e.g., with Ctrl+C).
    """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

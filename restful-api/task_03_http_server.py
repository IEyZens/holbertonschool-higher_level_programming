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
        # Check the requested path and respond accordingly
        if self.path == "/":

            # Respond with a welcome message
            self.send_response(200)
            # Set the content type to plain text
            self.send_header("Content-Type", "text/plain")
            # Send the response headers
            self.end_headers()
            # Write the response body
            self.wfile.write(b"Hello, this is a simple API!")

        # elif self.path == "/users":
        # Handle the /data endpoint
        elif self.path == "/data":

            # Respond with a JSON object containing user data
            self.send_response(200)
            # Set the content type to application/json
            self.send_header("Content-Type", "application/json")
            # Send the response headers
            self.end_headers()
            # Create a sample JSON response
            # This could be replaced with dynamic data retrieval in a real application
            data_response = {"name": "John", "age": 30, "city": "New York"}
            # Write the JSON response body
            # Convert the dictionary to a JSON string and encode it to bytes
            self.wfile.write(json.dumps(data_response).encode("utf-8"))

        # elif self.path.startswith("/users/"):
        # Handle the /status endpoint
        elif self.path == "/status":

            # Respond with a plain text "OK" message
            self.send_response(200)
            # Set the content type to plain text
            self.send_header("Content-Type", "text/plain")
            # Send the response headers
            self.end_headers()
            # Write the response body
            self.wfile.write(b"OK")

        # elif self.path.startswith("/users/"):
        # Handle the /info endpoint
        elif self.path == "/info":

            # Respond with API metadata in JSON format
            self.send_response(200)
            # Set the content type to application/json
            self.send_header("Content-Type", "application/json")
            # Send the response headers
            self.end_headers()
            # Create a sample JSON response with API metadata
            # This could include version, description, or other relevant information
            info_response = {"version": "1.0", "description": "A simple API built with http.server"}
            # Write the JSON response body
            # Convert the dictionary to a JSON string and encode it to bytes
            self.wfile.write(json.dumps(info_response).encode("utf-8"))

        # Handle any other endpoint
        else:

            # Respond with a 404 Not Found error
            # This indicates that the requested endpoint does not exist
            self.send_response(404)
            # Set the content type to plain text
            self.send_header("Content-type", "text/plain")
            # Send the response headers
            self.end_headers()
            # Write the response body with an error message
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
    # Create a server address tuple with an empty string for the host
    # This means the server will listen on all available interfaces
    server_address = ("", port)
    # Create an instance of the server with the specified address and handler
    httpd = server_class(server_address, handler_class)
    # Print a message indicating the server is running
    print(f"Server running on port {port}...")
    # Start the server and keep it running
    # The server will handle incoming requests using the specified handler class
    httpd.serve_forever()

# This block checks if the script is being run directly
# If so, it calls the run function to start the server
if __name__ == "__main__":
    # Call the run function to start the HTTP server
    run()

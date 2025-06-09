#!/usr/bin/python3
"""
This module implements a simple HTTP API using Python's built-in http.server
module.

It defines a custom request handler that supports multiple endpoints:
- `/` returns a welcome message
- `/data` returns a sample JSON object
- `/status` returns a simple OK message
- `/info` returns API metadata
- All other endpoints return a 404 error with an appropriate message

The server is intended for learning purposes and demonstrates basic HTTP
request handling in Python.
"""
import http.server
import json


class HttpServer(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler that defines behavior for GET requests.

    It handles multiple paths and returns either plain text or JSON responses.
    The handler also manages proper HTTP status codes and headers for each
    route.
    """

    def do_GET(self):
        """
        Handles GET requests for specific API endpoints.

        Depending on the request path, returns:
        - JSON data for `/data`
        - A text message for `/`
        - A simple OK message for `/status`
        - JSON metadata for `/info`
        - A 404 error message for any unknown path
        """
        if self.path == "/data":
            user_info = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_data = json.dumps(user_info).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_data)

        elif self.path == "/":
            response = {"message": "Hello, this is a simple API!"}

            json_bytes = json.dumps(response).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_bytes)

        elif self.path == "/status":
            message = {"status": "OK"}

            json_bytes = json.dumps(message).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_bytes)

        elif self.path == "/info":
            api_metadata = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            json_bytes = json.dumps(api_metadata).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_bytes)

        else:
            print("404 Not Found")

            error_message = {"error": "Endpoint not found"}
            json_bytes = json.dumps(error_message).encode("utf-8")
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_bytes)


"""
Starts the HTTP server using the custom HttpServer handler.

The server listens on all interfaces (0.0.0.0) at port 8000 and
handles incoming GET requests based on defined routes. It runs
indefinitely until manually interrupted (e.g., Ctrl+C).
"""

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, HttpServer)
    print("🚀 Server running at http://localhost:8000")
    httpd.serve_forever()

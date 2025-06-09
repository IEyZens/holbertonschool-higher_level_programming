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


class httpserver(http.server.BaseHTTPRequestHandler):
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
        print("Hello, this is a simple API!")

        if self.path == "/data":
            dict1 = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            bytes1 = json.dumps(dict1).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes1)

        elif self.path == "/":
            print("Hello, this is a simple API!")

            bytes2 = json.dumps("Hello, this is a simple API!").encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes2)

        elif self.path == "/status":
            message = "OK"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/info":
            dict3 = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            bytes3 = json.dumps(dict3).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes3)

        else:
            print("404 Not Found")

            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))

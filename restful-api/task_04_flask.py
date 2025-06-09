#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

# Create an instance of the Flask class
app = Flask(__name__)

@app.route("/")
def home():
    """
    Root endpoint that returns a welcome message.
    """
    return "Welcome to the Flask API!"

# In-memory storage for user data (no persistence)
users = {}

@app.route("/data")
def data():
    """
    Returns a list of all registered usernames.
    """
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """
    Simple health check endpoint.
    """
    return "OK"

@app.route("/users/<username>")
def user(username):
    """
    Returns the full user data for a given username.
    If the user does not exist, returns a 404 error.

    Parameters:
    - username (str): the username to look up
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user from the JSON request body.
    The "username" field is required; otherwise returns 400 error.

    Returns 201 Created on success with a confirmation message.
    """
    data = request.get_json()

    # Check if the request body contains JSON and a "username" field
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    # Store the entire user object
    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    # Run the development server on localhost:5000
    app.run()

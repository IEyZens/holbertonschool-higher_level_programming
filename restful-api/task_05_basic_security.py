#!/usr/bin/python3
"""
A Flask API implementing both Basic Auth and JWT authentication,
including role-based access and custom error handling.
"""
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify user credentials for Basic Auth.
    """
    if username in users and check_password_hash(users[username]["password"], password):
        return username


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Protected route using Basic Authentication.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Login route for generating JWT token.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in users and check_password_hash(users[username]["password"], password):
        token = create_access_token(identity=username)
        return jsonify({"access_token": token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Protected route using JWT authentication.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    JWT-protected route only accessible to admin users.
    """
    user = get_jwt_identity()
    if users[user]["role"] == "admin":
        return "Admin Access: Granted"
    else:
        return {"error": "Admin access required"}, 403


if __name__ == "__main__":
    app.config["JWT_SECRET_KEY"] = "your-secret-key"
    app.run()

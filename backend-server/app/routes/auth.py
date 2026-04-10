from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    return jsonify({"message": "User registered (placeholder)"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    return jsonify({"message": "User logged in (placeholder)"})

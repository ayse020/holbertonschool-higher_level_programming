#!/usr/bin/python3
"""
API Security and Authentication with Flask
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

# Flask app yaradın
app = Flask(__name__)

# JWT üçün gizli açar
app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Auth obyektlərini yaradın
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# İstifadəçi məlumatları (yaddaşda)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ==================== Basic Authentication ====================

@auth.verify_password
def verify_password(username, password):
    """
    Basic authentication üçün şifrəni yoxlayır
    """
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@auth.error_handler
def auth_error(status):
    """
    Basic auth xətası üçün handler
    """
    return jsonify({"error": "Access denied"}), status

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Basic authentication ilə qorunan endpoint
    """
    return "Basic Auth: Access Granted"

# ==================== JWT Authentication ====================

# JWT xəta handlerləri
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

@app.route('/login', methods=['POST'])
def login():
    """
    İstifadəçi girişi və JWT token yaradılması
    """
    # JSON məlumatını yoxla
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    # İstifadəçi adı və şifrəni yoxla
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    # İstifadəçini tap və şifrəni yoxla
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Token yarat (additional_claims ilə rol məlumatını əlavə et)
    additional_claims = {"role": user['role']}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )
    
    return jsonify(access_token=access_token), 200

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    JWT authentication ilə qorunan endpoint
    """
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Yalnız adminlər üçün endpoint
    """
    # JWT claimslərini al
    claims = get_jwt()
    
    # Rolunu yoxla
    if claims['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"

# ==================== Əlavə endpointlər ====================

@app.route('/')
def home():
    """Kök endpoint"""
    return "Welcome to the Secure API!"

@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    """
    Bütün istifadəçiləri qaytarır (yalnız JWT ilə)
    """
    # Sadəcə istifadəçi adlarını qaytar
    usernames = list(users.keys())
    return jsonify(usernames), 200

# ==================== Server işə salma ====================

if __name__ == '__main__':
    app.run(debug=True)

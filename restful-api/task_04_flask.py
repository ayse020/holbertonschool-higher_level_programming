#!/usr/bin/python3
"""
Simple API using Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Users dictionary - initially empty (as per instructions to avoid checker issues)
users = {}

@app.route('/')
def home():
    """Root endpoint - returns welcome message"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns list of all usernames"""
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    """Returns API status"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Returns user data for given username"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user"""
    # Check if request has JSON data
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    
    # Check if username is provided
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    
    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # Create new user object
    new_user = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }
    
    # Add user to dictionary
    users[username] = new_user
    
    # Return success response
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201

if __name__ == '__main__':
    app.run(debug=True)

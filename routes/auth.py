from flask import Blueprint, request, jsonify
from models.user import User
from models.database import add_user

# Create blueprint
auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        # Validate input
        user = User(username, email, password)
        if not user.is_valid():
            return jsonify({'error': 'Invalid email or password'}), 400
        
        # Add to database
        result = add_user(username, email, password)
        if not result:
            return jsonify({'error': 'Username already exists'}), 400
        
        # Success
        return jsonify({
            'message': 'User registered successfully',
            'user': username
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

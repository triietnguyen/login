from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from models.user_model import get_user_by_username

def ctl_login(data):
    username = data.get('username')
    password = data.get('password')
    
    user = get_user_by_username(username)
    
    if user and user['password'] == password:
        access_token = create_access_token(identity=user)
        refresh_token = create_refresh_token(identity=user)
        return jsonify({
            "success": True,
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": refresh_token
        }),200
    return jsonify({"success": False, "message": "Invalid credentials"}), 401


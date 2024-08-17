from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from controllers.user_controller import ctl_login

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return ctl_login(request.get_json())
    return render_template('login.html')

@user_bp.route('/home', methods=['GET'])
@jwt_required()
def home():
    return render_template('home.html')

@user_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify({"message": "Logged out successfully"}), 200



@user_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
from flask import Blueprint, request, jsonify

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Lógica de autenticación (puedes usar la base de datos aquí)
    if username == 'admin' and password == 'admin':
        return jsonify({"status": "success", "token": "fake-jwt-token"}), 200
    else:
        return jsonify({"status": "fail", "message": "Invalid credentials"}), 403

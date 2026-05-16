from flask import Blueprint, request, jsonify
from modules.receptionists_module import get_receptionists as fetch_receptionists
from modules.receptionists_module import (
    register_receptionist, 
    receptionist_login, 
    get_patients, 
    get_appointments,
    get_receptionists
)

receptionists_bp = Blueprint("receptionists", __name__)

# 1. Registration Route
@receptionists_bp.route("/receptionists/register", methods=["POST"])
def register():
    data = request.json
    if not data:
        return jsonify({"message": "No data provided"}), 400
    
    result = register_receptionist(data)
    return jsonify(result), 201

# 2. Login Route
@receptionists_bp.route("/receptionists/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    receptionist = receptionist_login(username, password)

    if receptionist:
        return jsonify({"message": "Login successful", "receptionist": receptionist}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

# 3. View Patients Route
@receptionists_bp.route("/receptionists/patients", methods=["GET"])
def view_patients():
    patients = get_patients()
    return jsonify(patients), 200

# 4. View Appointments Route
@receptionists_bp.route("/receptionists/appointments", methods=["GET"])
def view_appointments():
    appointments = get_appointments()
    return jsonify(appointments), 200

@receptionists_bp.route("/receptionists", methods=["GET"])
def get_receptionists():
    data = fetch_receptionists()
    return jsonify(data)
from flask import Blueprint, request, jsonify
from modules.patient_module import register_patient, get_all_patients, patient_login

# The name "patients" here is just an internal label for Flask
patient_bp = Blueprint("patients", __name__)

#patient registeration

@patient_bp.route("/patient/register", methods=["POST"])
def register_patient_route():
    data = request.json

    if not data:
        return jsonify({"message": "No data received"}), 400

    register_patient(data)

    # Adding 201 status code (Created)
    return jsonify({"message": "Patient registered successfully"}), 201

#patient login 

@patient_bp.route("/patient/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    patient = patient_login(username, password)

    if patient:
        return jsonify({
            "message": "Login successful",
            "user": patient
        }), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401
    
# FIX 2: Consistency - keep the GET route matching the pattern
@patient_bp.route("/patient/all", methods=["GET"])
def get_patients():
    patients = get_all_patients()
    return jsonify(patients)
from flask import Blueprint, request, jsonify
from modules.appointment_module import book_appointment
from modules.appointment_module import get_queue_data
from modules.appointment_module import get_patient_token
from utils import get_next_token
appointment_bp = Blueprint("appointment", __name__)

@appointment_bp.route("/book_appointment", methods=["POST"])
def create_appointment():

    data = request.json

    print("DATA RECEIVED:", data)
    token = get_next_token(
        data.get("doctor_id"),
        data.get("appointment_date")
    )

    data["token_number"] = token

    result = book_appointment(data)

    return jsonify(result)

@appointment_bp.route("/queue", methods=["GET"])
def get_queue():
    data = get_queue_data()
    return jsonify(data)

@appointment_bp.route("/my_token/<int:patient_id>", methods=["GET"])
def my_token(patient_id):
    data = get_patient_token(patient_id)

    if not data:
        return jsonify({"message": "No appointment found"}), 404

    return jsonify(data)
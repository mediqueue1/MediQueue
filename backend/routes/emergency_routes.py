from flask import Blueprint, request, jsonify

from modules.emergency_module import (
    add_emergency_case,
    get_emergency_cases,
    update_priority,
    delete_emergency
)

emergency_bp = Blueprint("emergency_bp", __name__)


# ADD EMERGENCY
@emergency_bp.route("/emergency/add", methods=["POST"])
def create_emergency():

    data = request.json

    result = add_emergency_case(
        data.get("patient_id"),
        data.get("doctor_id"),
        data.get("priority_level"),
        data.get("description")
    )

    return jsonify(result)


# VIEW EMERGENCIES
@emergency_bp.route("/emergency", methods=["GET"])
def view_emergencies():

    emergencies = get_emergency_cases()

    return jsonify(emergencies)


# UPDATE PRIORITY
@emergency_bp.route("/emergency/priority/<int:emergency_id>", methods=["PUT"])
def change_priority(emergency_id):

    data = request.json

    result = update_priority(
        emergency_id,
        data.get("priority_level")
    )

    return jsonify(result)


# DELETE EMERGENCY
@emergency_bp.route("/emergency/<int:emergency_id>", methods=["DELETE"])
def remove_emergency(emergency_id):

    result = delete_emergency(emergency_id)

    return jsonify(result)
from flask import Blueprint, request, jsonify
from datetime import date
from modules.queue_module import (
    add_patient_queue,
    view_queue,
    call_next_patient,
    complete_consultation,
    get_waiting_count
)

queue_bp = Blueprint("queue_bp", __name__)

# ADD PATIENT TO QUEUE
@queue_bp.route("/queue/add", methods=["POST"])
def add_patient():

    data = request.json

    result = add_patient_queue(
        data.get("patient_id"),
        data.get("doctor_id")
    )

    return jsonify(result)

# VIEW QUEUE
@queue_bp.route("/queue", methods=["GET"])
def get_queue():

    queue = view_queue()

    return jsonify(queue)

# CALL NEXT PATIENT
@queue_bp.route("/queue/next/<int:doctor_id>", methods=["PUT"])
def next_patient(doctor_id):

    patient = call_next_patient(doctor_id)

    if not patient:
        return jsonify({"message": "No patients waiting"})

    return jsonify({
        "message": "Next patient called",
        "patient": patient
    })

# COMPLETE CONSULTATION
@queue_bp.route("/queue/complete/<int:token_id>", methods=["PUT"])
def finish_consultation(token_id):

    result = complete_consultation(token_id)

    return jsonify(result)

@queue_bp.route("/queue/waiting_count/<int:doctor_id>", methods=["GET"])
def waiting_count(doctor_id):

    count = get_waiting_count(doctor_id)

    return jsonify({
        "doctor_id": doctor_id,
        "waiting_patients": count
    })

# @queue_bp.route("/queue/waiting_time/<int:doctor_id>", methods=["GET"])
# def waiting_time(doctor_id):

#     today = date.today()
#     time = calculate_waiting_time(doctor_id, today)

#     return jsonify({
#         "doctor_id": doctor_id,
#         "estimated_waiting_time": time
#     })
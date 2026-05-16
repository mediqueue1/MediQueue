from flask import Blueprint, request, jsonify

from modules.medical_record_module import (
    add_medical_record,
    get_medical_records,
    get_patient_records,
    delete_medical_record
)

medical_record_bp = Blueprint("medical_record_bp", __name__)


# ADD MEDICAL RECORD
@medical_record_bp.route("/medical_record/add", methods=["POST"])
def create_record():

    data = request.json

    result = add_medical_record(
        data.get("patient_id"),
        data.get("doctor_id"),
        data.get("diagnosis"),
        data.get("prescription"),
        data.get("visit_date")
    )

    return jsonify(result)


# VIEW ALL RECORDS
@medical_record_bp.route("/medical_records", methods=["GET"])
def view_records():

    records = get_medical_records()

    return jsonify(records)


# VIEW PATIENT HISTORY
@medical_record_bp.route("/medical_records/patient/<int:patient_id>", methods=["GET"])
def patient_history(patient_id):

    records = get_patient_records(patient_id)

    return jsonify(records)


# DELETE RECORD
@medical_record_bp.route("/medical_record/<int:record_id>", methods=["DELETE"])
def remove_record(record_id):

    result = delete_medical_record(record_id)

    return jsonify(result)
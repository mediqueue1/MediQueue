from flask import Blueprint, request, jsonify
from flask import session
from modules.admin_module import get_admin_by_id
from modules.admin_module import get_counts
from modules.admin_module import (
    admin_login,
    add_doctor,
    get_doctors,
    delete_doctor,
    get_patients,
    get_appointments,
    register_admin
)

admin_bp = Blueprint("admin_bp", __name__)


# ADMIN LOGIN
@admin_bp.route("/admin/login", methods=["POST"])
def admin_login_route():
    data = request.json
    admin = admin_login(data.get("username"), data.get("password"))

    if admin:
        session["admin_id"] = admin["admin_id"]
        
        # Construct the full name here
        full_name = " ".join(filter(None, [
            admin.get("first_name"),
            admin.get("middle_name"),
            admin.get("last_name")
        ]))

        return jsonify({
            "message": "Login successful",
            "admin_id": admin["admin_id"],
            "name": full_name  # Send the name back!
        })

    return jsonify({"message": "Invalid credentials"}), 401

# REGISTER ADMIN
@admin_bp.route("/admin/register", methods=["POST"])
def create_admin():
    data = request.json
    result = register_admin(data)
    return jsonify(result)

# ADD DOCTOR
@admin_bp.route("/admin/add_doctor", methods=["POST"])
def create_doctor():

    data = request.json

    result = add_doctor(data)

    return jsonify(result)


# VIEW DOCTORS
@admin_bp.route("/admin/doctors", methods=["GET"])
def view_doctors():

    doctors = get_doctors()

    return jsonify({
        "doctors": doctors
    })


# DELETE DOCTOR
@admin_bp.route("/admin/delete_doctor/<int:doctor_id>", methods=["DELETE"])
def remove_doctor(doctor_id):

    result = delete_doctor(doctor_id)

    return jsonify(result)


# VIEW PATIENTS
@admin_bp.route("/admin/patients", methods=["GET"])
def view_all_patients():

    patients = get_patients()

    return jsonify({
        "patients": patients
    })


# VIEW APPOINTMENTS
@admin_bp.route("/admin/appointments", methods=["GET"])
def view_all_appointments():

    appointments = get_appointments()

    return jsonify({
        "appointments": appointments
    })

# TOTAL PATIENTS AND DOCTORS AND TODAY'S APPOINTMENTS
@admin_bp.route("/admin/counts", methods=["GET"])
def counts():
    return jsonify(get_counts())

#Admin Login Name
@admin_bp.route("/admin/dashboard", methods=["GET"])
def admin_dashboard():

    admin_id = session.get("admin_id")
    

    if not admin_id:
        return jsonify({"message": "Not logged in"}), 401

    admin = get_admin_by_id(admin_id)

    if not admin:
        return jsonify({"message": "Admin not found"}), 404

    full_name = " ".join(filter(None, [
        admin["first_name"],
        admin["middle_name"],
        admin["last_name"]
    ]))

    return jsonify({"name": full_name})
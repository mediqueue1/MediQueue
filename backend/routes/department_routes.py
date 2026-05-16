from flask import Blueprint, request, jsonify

from modules.department_module import (
    add_department,
    get_departments,
    update_department,
    delete_department
)

department_bp = Blueprint("department_bp", __name__)


# ADD DEPARTMENT
@department_bp.route("/departments/add", methods=["POST"])
def create_department():

    data = request.json

    result = add_department(
        data.get("department_name"),
        data.get("description")
    )

    return jsonify(result)


# VIEW ALL DEPARTMENTS
@department_bp.route("/departments", methods=["GET"])
def view_departments():

    departments = get_departments()

    return jsonify(departments)


# UPDATE DEPARTMENT
@department_bp.route("/departments/<int:department_id>", methods=["PUT"])
def edit_department(department_id):

    data = request.json

    result = update_department(
        department_id,
        data.get("department_name"),
        data.get("description")
    )

    return jsonify(result)


# DELETE DEPARTMENT
@department_bp.route("/departments/<int:department_id>", methods=["DELETE"])
def remove_department(department_id):

    result = delete_department(department_id)

    return jsonify(result)
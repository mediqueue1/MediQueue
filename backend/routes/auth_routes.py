from flask import Blueprint, request
from modules.auth_module import register_user, login_user, reset_password

auth_bp = Blueprint("auth", __name__)

# REGISTER
@auth_bp.route("/auth/register", methods=["POST"])
def register():

    data = request.json

    return register_user(
        data["username"],
        data["email"],
        data["password"],
        data["role"]
    )


# LOGIN
@auth_bp.route("/auth/login", methods=["POST"])
def login():

    data = request.json

    user = login_user(data["username"], data["password"])

    if user:
        return {
            "message": "Login successful",
            "role": user["role"],
            "user_id": user["user_id"]
        }

    return {"message": "Invalid username or password"}


# FORGOT PASSWORD
@auth_bp.route("/auth/forgot-password", methods=["POST"])
def forgot_password():

    data = request.json

    return reset_password(
        data["email"],
        data["new_password"]
    )
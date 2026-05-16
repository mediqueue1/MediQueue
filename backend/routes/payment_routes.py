from flask import Blueprint, request, jsonify

payment_bp = Blueprint("payments", __name__)

@payment_bp.route("/pay", methods=["POST"])
def payments():
    return jsonify({"message": "Payment processed successfully"})
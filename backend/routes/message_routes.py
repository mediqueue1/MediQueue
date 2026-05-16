from flask import Blueprint, request, jsonify
from modules.message_module import send_message, get_inbox

message_bp = Blueprint("message_bp", __name__)


# SEND MESSAGE
@message_bp.route("/send", methods=["POST"])
def create_message():

    data = request.json

    result = send_message(data)

    return jsonify(result), 201


# GET INBOX
@message_bp.route("/inbox/<u_type>/<int:u_id>", methods=["GET"])
def inbox(u_type, u_id):

    messages = get_inbox(u_type, u_id)

    return jsonify(messages)
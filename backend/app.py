from flask import Flask
from flask_cors import CORS

from routes.receptionists_routes import receptionists_bp
from routes.admin_routes import admin_bp
from routes.patient_routes import patient_bp
from routes.doctor_routes import doctor_bp
from routes.appointment_routes import appointment_bp
from routes.auth_routes import auth_bp
from routes.payment_routes import payment_bp
from routes.message_routes import message_bp
from routes.queue_routes import queue_bp
from routes.emergency_routes import emergency_bp
from routes.medical_record_routes import medical_record_bp
from routes.department_routes import department_bp

app = Flask(__name__)
app.secret_key = "anything"
# CORS(app, supports_credentials=True, origins=["http://127.0.0.1:5500", "http://localhost:5500"])
CORS(app, supports_credentials=True, origins=["https://mediqueue01.netlify.app"])

app.register_blueprint(receptionists_bp, url_prefix="/api")
app.register_blueprint(admin_bp, url_prefix="/api")
app.register_blueprint(patient_bp, url_prefix="/api")
# app.register_blueprint(doctor_bp)
# app.register_blueprint(appointment_bp)
app.register_blueprint(auth_bp)
# app.register_blueprint(payment_bp, url_prefix="/payments")
# app.register_blueprint(message_bp, url_prefix="/messages")
app.register_blueprint(queue_bp)
app.register_blueprint(emergency_bp)
app.register_blueprint(medical_record_bp)
app.register_blueprint(department_bp)

app.register_blueprint(doctor_bp, url_prefix="/api")
app.register_blueprint(appointment_bp, url_prefix="/api")
app.register_blueprint(payment_bp, url_prefix="/payments")
app.register_blueprint(message_bp, url_prefix="/messages")

@app.route("/")
def home():
    return {"message": "Hospital Queue & Token Management Backend Running"}

if __name__ == "__main__":
    # app.run(debug=True)
     app.run(host="0.0.0.0", port=5000, debug=True)

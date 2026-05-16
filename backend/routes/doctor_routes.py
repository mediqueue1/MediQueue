from flask import Blueprint, request, jsonify
from modules.doctor_module import get_doctors, register_doctor, doctor_login, get_db_connection

doctor_bp = Blueprint("doctors_api_unique", __name__)

# 1. REGISTER DOCTOR
@doctor_bp.route("/doctors/register", methods=["POST"])
def register():
    data = request.json
    result = register_doctor(data)
    return jsonify(result), 201


# 2. DOCTOR LOGIN
@doctor_bp.route("/doctors/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    doctor = doctor_login(username, password)

    if doctor:
        return jsonify({
            "message": "Login successful",
            "user": doctor
        }), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401


# 4. FETCH ALL DOCTORS
@doctor_bp.route("/doctors", methods=["GET"])
def fetch_doctors():
    doctors = get_doctors()
    return jsonify(doctors)


# 5. QUEUE STATUS (UNCHANGED)
@doctor_bp.route('/queue_status/<int:patient_id>', methods=['GET'])
def get_queue_status(patient_id):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # ✅ Get latest appointment
        cursor.execute("""
            SELECT a.token_number, a.doctor_id, d.first_name, d.last_name, d.specialization
            FROM appointments a
            JOIN doctors d ON a.doctor_id = d.doctor_id
            WHERE a.patient_id = %s AND a.appointment_date = CURDATE()
            ORDER BY a.appointment_id DESC LIMIT 1
        """, (patient_id,))
        appointment = cursor.fetchone()

        if not appointment:
            return jsonify({"success": False, "message": "No appointment today"})

        # ✅ Get current serving
        cursor.execute("""
            SELECT MIN(token_number) as serving 
            FROM appointments 
            WHERE doctor_id = %s 
              AND appointment_date = CURDATE() 
              AND status = 'scheduled'
        """, (appointment['doctor_id'],))
        serving_data = cursor.fetchone()

        current_serving = serving_data['serving'] if serving_data['serving'] is not None else appointment['token_number']
        tokens_ahead = appointment['token_number'] - current_serving

        # ✅ NEW: average consultation time
        cursor.execute("""
            SELECT AVG(consultation_duration) AS avg_time
            FROM appointments
            WHERE doctor_id = %s
              AND consultation_duration IS NOT NULL
        """, (appointment['doctor_id'],))

        avg_data = cursor.fetchone()
        avg_time = avg_data['avg_time'] if avg_data['avg_time'] else 10

        # ✅ waiting time
        waiting_time = max(0, tokens_ahead) * avg_time

        # ✅ FINAL RESPONSE
        return jsonify({
            "success": True,
            "user_token": appointment['token_number'],
            "current_serving": current_serving,
            "tokens_ahead": max(0, tokens_ahead),
            "waiting_time": int(waiting_time),
            "doctor_name": f"{appointment['first_name']} {appointment['last_name']}"
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# =========================================================
# ✅ ADDED: NEXT PATIENT (QUEUE LOGIC USING APPOINTMENTS)
# =========================================================
@doctor_bp.route('/queue/next/<int:doctor_id>', methods=['GET'])
def get_next_patient(doctor_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Get next scheduled patient
        cursor.execute("""
    SELECT 
    a.appointment_id,
    a.full_name,
    a.token_number
FROM appointments a
WHERE a.doctor_id = %s
  AND DATE(a.appointment_date) = CURDATE()
  AND a.status = 'scheduled'
ORDER BY a.token_number ASC
LIMIT 1
""", (doctor_id,))

        patient = cursor.fetchone()

        if not patient:
            return jsonify({"patient": None})

        # mark as in consultation
        cursor.execute("""
    UPDATE appointments
    SET 
        status = 'in_consultation',
        consultation_start = NOW()
    WHERE appointment_id = %s
""", (patient["appointment_id"],))

        conn.commit()

        return jsonify({"patient": patient})

    finally:
        cursor.close()
        conn.close()


# =========================================================
# ✅ ADDED: COMPLETE PATIENT
# =========================================================
@doctor_bp.route('/queue/complete/<int:appointment_id>', methods=['PUT'])
def complete_appointment(appointment_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
    UPDATE appointments
    SET 
        status = 'completed',
        consultation_end = NOW(),
        consultation_duration = TIMESTAMPDIFF(MINUTE, consultation_start, NOW())
    WHERE appointment_id = %s
""", (appointment_id,))

        conn.commit()

        return jsonify({"success": True, "message": "Appointment completed"})

    finally:
        cursor.close()
        conn.close()

@doctor_bp.route('/queue_status_all/<int:patient_id>', methods=['GET'])
def get_all_queue_status(patient_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT appointment_id, token_number, doctor_id, status
            FROM appointments
            WHERE patient_id = %s AND appointment_date = CURDATE()
            ORDER BY token_number ASC
        """, (patient_id,))

        appointments = cursor.fetchall()

        if not appointments:
            return jsonify({"success": False, "message": "No appointments today"})

        result = []

        for appt in appointments:
            cursor.execute("""
                SELECT COUNT(*) AS ahead
                FROM appointments
                WHERE doctor_id = %s
                  AND appointment_date = CURDATE()
                  AND token_number < %s
                  AND status IN ('scheduled', 'in_consultation')
            """, (appt["doctor_id"], appt["token_number"]))

            ahead = cursor.fetchone()["ahead"]

            result.append({
                "token_number": appt["token_number"],
                "tokens_ahead": ahead,
                "status": appt["status"]
            })

        return jsonify({
            "success": True,
            "appointments": result
        })

    finally:
        cursor.close()
        conn.close()


#now serving on Receptionists dashboard

@doctor_bp.route('/now_serving', methods=['GET'])
def now_serving():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT 
                a.token_number,
                a.full_name,
                a.status,
                d.first_name,
                d.last_name,
                d.specialization
            FROM appointments a
            JOIN doctors d ON a.doctor_id = d.doctor_id
            WHERE a.status IN ('in_consultation', 'scheduled')
            ORDER BY 
                CASE 
                    WHEN a.status = 'in_consultation' THEN 1
                    ELSE 2
                END,
                a.token_number ASC
            LIMIT 1
        """)

        data = cursor.fetchall()

        return jsonify({
            "success": True,
            "data": data
        })

    finally:
        cursor.close()
        conn.close()
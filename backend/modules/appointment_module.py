from database import get_db_connection

def book_appointment(data):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
INSERT INTO appointments (
    patient_id,
    doctor_id,
    doctor_name,
    full_name,
    contact,
    gender,
    dob,
    appointment_date,
    appointment_time,
    status,
    token_number
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

    cursor.execute(query, (
        data.get("patient_id"),
        data.get("doctor_id"),
        data.get("doctor_name"),
        data.get("full_name"),
        data.get("contact"),
        data.get("gender"),
        data.get("dob"),
        data.get("appointment_date"),
        data.get("appointment_time"),
        "scheduled",
        data.get("token_number")
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return {"success": True, "message": "Appointment booked successfully"}

def get_queue_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT 
        appointment_id,
        patient_id,
        doctor_id,
        full_name,
        appointment_date,
        appointment_time,
        token_number,
        doctor_name, 
        status
    FROM appointments
    WHERE LOWER(TRIM(status)) IN ('scheduled', 'in_consultation') 
    ORDER BY appointment_date DESC, appointment_time ASC
    """
#if you want only today appointment in the queue then use this query after FROM appointments====>WHERE appointment_date = CURDATE()

    cursor.execute(query)
    data = cursor.fetchall()
    #vFIX: Convert date/time to string
    for row in data:
        for key, value in row.items():
            if hasattr(value, "isoformat"):
                row[key] = value.isoformat()
            elif str(type(value)).endswith("timedelta'>"):
                row[key] = str(value)

    cursor.close()
    conn.close()

    return data

def get_patient_token(patient_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Get today's appointment for this patient
    query = """
    SELECT token_number, doctor_id, appointment_date
    FROM appointments
    WHERE patient_id = %s AND appointment_date = CURDATE()
    """
    cursor.execute(query, (patient_id,))
    patient = cursor.fetchone()

    if not patient:
        return None

    # Count how many patients are ahead
    query2 = """
    SELECT COUNT(*) AS ahead
    FROM appointments
    WHERE doctor_id = %s
    AND appointment_date = %s
    AND token_number < %s
    """
    cursor.execute(query2, (
        patient["doctor_id"],
        patient["appointment_date"],
        patient["token_number"]
    ))

    ahead = cursor.fetchone()["ahead"]

    cursor.close()
    conn.close()

    return {
        "token_number": patient["token_number"],
        "ahead": ahead
    }
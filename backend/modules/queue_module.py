from database import get_db_connection
from datetime import date

# ADD PATIENT TO QUEUE (GENERATE TOKEN)

def add_patient_queue(patient_id, doctor_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    today = date.today()

    # Get last token number for the doctor today
    query = """
    SELECT MAX(token_number) FROM queue_tokens
    WHERE doctor_id=%s AND visit_date=%s
    """

    cursor.execute(query, (doctor_id, today))
    result = cursor.fetchone()[0]

    next_token = 1 if result is None else result + 1

    insert_query = """
    INSERT INTO queue_tokens (patient_id, doctor_id, token_number, visit_date)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(insert_query, (patient_id, doctor_id, next_token, today))
    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "Patient added to queue",
        "token_number": next_token
    }

# VIEW QUEUE

def view_queue():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT 
        qt.token_id,
        qt.token_number,
        qt.status,
        qt.doctor_id,
        qt.patient_id,
        p.first_name,
        p.last_name,
        d.first_name AS doctor_name
    FROM queue_tokens qt
    JOIN patients p ON qt.patient_id = p.patient_id
    JOIN doctors d ON qt.doctor_id = d.doctor_id
    ORDER BY qt.token_number
    """

    cursor.execute(query)

    queue = cursor.fetchall()

    cursor.close()
    conn.close()

    return queue

# CALL NEXT PATIENT

def call_next_patient(doctor_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT * FROM queue_tokens
    WHERE doctor_id=%s AND status='waiting'
    ORDER BY token_number
    LIMIT 1
    """

    cursor.execute(query, (doctor_id,))
    patient = cursor.fetchone()

    if not patient:
        return None

    update_query = """
    UPDATE queue_tokens
    SET status='in_consultation'
    WHERE token_id=%s
    """

    cursor.execute(update_query, (patient["token_id"],))
    conn.commit()

    cursor.close()
    conn.close()

    return patient

# COMPLETE CONSULTATION

def complete_consultation(token_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    UPDATE queue_tokens
    SET status='completed'
    WHERE token_id=%s
    """

    cursor.execute(query, (token_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Consultation completed"}

# get waiting count

def get_waiting_count(doctor_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*)
    FROM queue_tokens
    WHERE doctor_id=%s AND status='waiting'
    """

    cursor.execute(query,(doctor_id,))
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count

# def get_average_time(doctor_id):
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     cursor.execute("""
#     SELECT AVG(TIMESTAMPDIFF(MINUTE, called_at, completed_at))
#     FROM queue_tokens
#     WHERE doctor_id=%s AND completed_at IS NOT NULL
#     """, (doctor_id,))

#     avg = cursor.fetchone()[0]

#     conn.close()

#     if avg is None:
#         return 5   # default time

#     return int(avg)


# def get_patients_ahead(doctor_id, date):
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     cursor.execute("""
#     SELECT COUNT(*)
#     FROM queue_tokens
#     WHERE doctor_id=%s AND visit_date=%s AND status='waiting'
#     """, (doctor_id, date))

#     count = cursor.fetchone()[0]

#     conn.close()
#     return count


# def calculate_waiting_time(doctor_id, visit_date):
#     patients_ahead = get_patients_ahead(doctor_id, visit_date)
#     avg_time = get_average_time(doctor_id)

#     return patients_ahead * avg_time
from database import get_db_connection
def get_next_token(doctor_id, date):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT IFNULL(MAX(token_number), 0) + 1
    FROM appointments
    WHERE doctor_id = %s AND appointment_date = %s
    """

    cursor.execute(query, (doctor_id, date))
    token = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return token
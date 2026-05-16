import datetime
from database import get_db_connection

# 1. Receptionist Registration
def register_receptionist(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO receptionists 
    (first_name, middle_name, last_name, phone, email, username, password) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    cursor.execute(query, (
        data.get("firstName"),
        data.get("middleName"),
        data.get("lastName"),
        data.get("phone"),
        data.get("email"),
        data.get("username"),
        data.get("password")
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Receptionist registered successfully"}


# 2. Receptionist Login
def receptionist_login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM receptionists WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    receptionist = cursor.fetchone()

    cursor.close()
    conn.close()

    return receptionist


# 3. Get Patient Details
def get_patients():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM patients")

    patients = cursor.fetchall()

    cursor.close()
    conn.close()

    return patients


# 4. Get Appointment Details
def get_appointments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM appointments")
    appointments = cursor.fetchall()

    #FIX: convert timedelta to string
    for app in appointments:
        for key, value in app.items():
            if isinstance(value, datetime.timedelta):
                app[key] = str(value)

    cursor.close()
    conn.close()

    return appointments

# 5. Get All Receptionists
def get_receptionists():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM receptionists")
    receptionists = cursor.fetchall()

    cursor.close()
    conn.close()

    return receptionists
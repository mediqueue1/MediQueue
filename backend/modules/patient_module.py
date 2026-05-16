import re
from database import get_db_connection

# Register patient

def register_patient(data):

    password = data.get("password")
    if not password:
        return {"success": False, "message": "Password is required"}

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{6,}$'

    if not re.match(pattern, password):
        return {
            "success": False,
            "message": "Password must contain uppercase, lowercase, number, special character and be at least 8 characters long"
        }

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO patients (first_name, middle_name, last_name, gender, date_of_birth, phone, email, address, username, password)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query,(
        data.get("firstName"),
        data.get("middleName"),
        data.get("lastName"),
        data.get("gender"),
        data.get("dateOfBirth"),
        data.get("phone"),
        data.get("email"),
        data.get("address"),
        data.get("username"),
        data.get("password")
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return True

def patient_login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Search the patients table for the username and password
    query = "SELECT * FROM patients WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    patient = cursor.fetchone()

    cursor.close()
    conn.close()

    return patient

# Get all patients

def get_all_patients():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()

    cursor.close()
    conn.close()

    return patients
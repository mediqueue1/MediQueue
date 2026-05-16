import datetime
import re 
from database import get_db_connection


# ✅ 1. REGISTER / ADD DOCTOR (MAIN FUNCTION)
def register_doctor(data):
    try:

        password = data.get("password")

        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

        if not password or not re.match(pattern, password):
            return {
                "success": False,
                "message": "Password must contain uppercase, lowercase, number, special character and be at least 8 characters long"
            }
        
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO doctors (
            first_name,
            middle_name,
            last_name,
            specialization,
            phone,
            email,
            department_id,
            available_from,
            available_to,
            username,
            password
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            data.get("first_name"),
            data.get("middle_name"),
            data.get("last_name"),
            data.get("specialization"),
            data.get("phone"),
            data.get("email"),
            data.get("department_id"),  # can be None
            data.get("available_from"),
            data.get("available_to"),
            data.get("username"),
            data.get("password")
        ))

        conn.commit()
        cursor.close()
        conn.close()

        return {"success": True, "message": "Doctor added successfully"}

    except Exception as e:
        print("ERROR:", e)
        return {"success": False, "message": str(e)}


# ✅ 2. GET ALL DOCTORS
def get_doctors():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM doctors")
        doctors = cursor.fetchall()

        # Convert time fields to string (for JSON)
        for doc in doctors:
            for key, value in doc.items():
                if isinstance(value, datetime.timedelta):
                    doc[key] = str(value)

        cursor.close()
        conn.close()

        return doctors if doctors else []

    except Exception as e:
        print(f"CRITICAL DATABASE ERROR: {e}")
        return []


# ✅ 3. DOCTOR LOGIN
def doctor_login(username, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM doctors WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))

        doctor = cursor.fetchone()
        if doctor:
            for key, value in doctor.items():
                if isinstance(value, datetime.timedelta):
                    doctor[key] = str(value)

        cursor.close()
        conn.close()

        return doctor

    except Exception as e:
        print("LOGIN ERROR:", e)
        return None
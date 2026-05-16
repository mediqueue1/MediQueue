from database import get_db_connection


def admin_login(username, password):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM admin WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    admin = cursor.fetchone()

    cursor.close()
    conn.close()

    return admin


def add_doctor(data):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO doctors
    (first_name, middle_name, last_name, specialization, phone)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(
        data.get("first_name"),
        data.get("middle_name"),
        data.get("last_name"),
        data.get("specialization"),
        data.get("phone")
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Doctor added successfully"}


def get_doctors():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM doctors")

    doctors = cursor.fetchall()

    cursor.close()
    conn.close()

    return doctors


def delete_doctor(doctor_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM doctors WHERE doctor_id=%s"

    cursor.execute(query,(doctor_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Doctor deleted successfully"}


def get_patients():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM patients")

    patients = cursor.fetchall()

    cursor.close()
    conn.close()

    return patients


def get_appointments():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM appointments")

    appointments = cursor.fetchall()

    cursor.close()
    conn.close()

    return appointments

def register_admin(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    # NOTE: Check your database! Ensure these column names match your 'admin' table perfectly.
    query = """
    INSERT INTO admin (first_name, middle_name, last_name, username, password, email, phone) 
    VALUES (%s, %s, %s, %s, %s,%s,%s)
    """
    
    # We grab the username and password sent from your JavaScript form
    cursor.execute(query, (
        data.get("firstName"),
        data.get("middleName"),
        data.get("lastName"),
        data.get("username"),
        data.get("password"),
        data.get("email"),
        data.get("phone")
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Admin registered successfully"}

def get_counts():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Count doctors
    cursor.execute("SELECT COUNT(*) FROM doctors")
    total_doctors = cursor.fetchone()[0]

    # Count patients
    cursor.execute("SELECT COUNT(*) FROM patients")
    total_patients = cursor.fetchone()[0]

    #Today's Appointments
    cursor.execute("""
        SELECT COUNT(*) FROM appointments 
        WHERE appointment_date = CURDATE() 
    """)
    #if you remove the above line then you will get the all appointments in the database

    today_appointments = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {
        "total_doctors": total_doctors,
        "total_patients": total_patients,
        "today_appointments": today_appointments
    }

def get_admin_by_id(admin_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT first_name, middle_name, last_name
        FROM admin
        WHERE admin_id = %s
    """, (admin_id,))

    admin = cursor.fetchone()

    cursor.close()
    conn.close()

    return admin
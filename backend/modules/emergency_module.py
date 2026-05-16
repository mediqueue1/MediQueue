from database import get_db_connection


# ADD EMERGENCY CASE
def add_emergency_case(patient_id, doctor_id, priority_level, description):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO emergency_cases
    (patient_id, doctor_id, priority_level, description)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(query,(patient_id, doctor_id, priority_level, description))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Emergency case added successfully"}


# VIEW ALL EMERGENCIES
def get_emergency_cases():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT 
        e.emergency_id,
        e.priority_level,
        e.description,
        e.arrival_time,
        p.first_name,
        p.last_name,
        d.first_name AS doctor_name
    FROM emergency_cases e
    JOIN patients p ON e.patient_id = p.patient_id
    JOIN doctors d ON e.doctor_id = d.doctor_id
    ORDER BY e.priority_level ASC, e.arrival_time ASC
    """

    cursor.execute(query)

    emergencies = cursor.fetchall()

    cursor.close()
    conn.close()

    return emergencies


# UPDATE PRIORITY
def update_priority(emergency_id, priority_level):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    UPDATE emergency_cases
    SET priority_level=%s
    WHERE emergency_id=%s
    """

    cursor.execute(query,(priority_level, emergency_id))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Priority updated successfully"}


# DELETE EMERGENCY
def delete_emergency(emergency_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM emergency_cases WHERE emergency_id=%s"

    cursor.execute(query,(emergency_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Emergency case removed"}
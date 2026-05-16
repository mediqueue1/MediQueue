from database import get_db_connection


# ADD MEDICAL RECORD
def add_medical_record(patient_id, doctor_id, diagnosis, prescription, visit_date):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO medical_records
    (patient_id, doctor_id, diagnosis, prescription, visit_date)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(patient_id, doctor_id, diagnosis, prescription, visit_date))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Medical record added successfully"}


# VIEW ALL MEDICAL RECORDS
def get_medical_records():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT 
        mr.record_id,
        mr.diagnosis,
        mr.prescription,
        mr.visit_date,
        p.first_name,
        p.last_name,
        d.first_name AS doctor_name
    FROM medical_records mr
    JOIN patients p ON mr.patient_id = p.patient_id
    JOIN doctors d ON mr.doctor_id = d.doctor_id
    ORDER BY mr.visit_date DESC
    """

    cursor.execute(query)

    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records


# VIEW RECORDS BY PATIENT
def get_patient_records(patient_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM medical_records
    WHERE patient_id=%s
    ORDER BY visit_date DESC
    """

    cursor.execute(query,(patient_id,))

    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records


# DELETE RECORD
def delete_medical_record(record_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM medical_records WHERE record_id=%s"

    cursor.execute(query,(record_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Medical record deleted successfully"}
from database import get_db_connection


# ADD DEPARTMENT
def add_department(department_name, description):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO departments (department_name, description)
    VALUES (%s,%s)
    """

    cursor.execute(query,(department_name, description))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Department added successfully"}


# GET ALL DEPARTMENTS
def get_departments():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM departments"

    cursor.execute(query)

    departments = cursor.fetchall()

    cursor.close()
    conn.close()

    return departments


# UPDATE DEPARTMENT
def update_department(department_id, department_name, description):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    UPDATE departments
    SET department_name=%s, description=%s
    WHERE department_id=%s
    """

    cursor.execute(query,(department_name, description, department_id))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Department updated successfully"}


# DELETE DEPARTMENT
def delete_department(department_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM departments WHERE department_id=%s"

    cursor.execute(query,(department_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message":"Department deleted successfully"}
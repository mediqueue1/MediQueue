from database import get_db_connection

# REGISTER USER
def register_user(username, email, password, role):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO users (username, email, password, role)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(query, (username, email, password, role))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "User registered successfully"}


# LOGIN USER
def login_user(username, password):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT * FROM users
    WHERE username=%s AND password=%s
    """

    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


# RESET PASSWORD
def reset_password(email, new_password):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    UPDATE users
    SET password=%s
    WHERE email=%s
    """

    cursor.execute(query, (new_password, email))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Password updated successfully"}
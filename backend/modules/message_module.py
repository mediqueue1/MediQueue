from database import get_db_connection


def send_message(data):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO messages 
    (sender_type, sender_id, receiver_type, receiver_id, subject, message_body)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        data['sender_type'],
        data['sender_id'],
        data['receiver_type'],
        data['receiver_id'],
        data['subject'],
        data['message_body']
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Message sent successfully"}


def get_inbox(user_type, user_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT * FROM messages
    WHERE receiver_type = %s AND receiver_id = %s
    ORDER BY sent_at DESC
    """

    cursor.execute(query, (user_type, user_id))

    messages = cursor.fetchall()

    cursor.close()
    conn.close()

    return messages
from database import get_db_connection

conn = get_db_connection()

if conn.is_connected():
    print("Database connected successfully")
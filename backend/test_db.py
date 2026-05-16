from modules.admin_module import get_db_connection # Adjust this import if needed

try:
    # Try to open the connection
    conn = get_db_connection()
    
    if conn.is_connected():
        print("✅ SUCCESS! The backend is successfully talking to the MySQL database.")
        
    # Close it politely
    conn.close()

except Exception as e:
    print("❌ FAILED! Could not connect to the database.")
    print("Error details:", e)
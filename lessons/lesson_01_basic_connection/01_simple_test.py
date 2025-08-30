import mysql.connector 
print("Lesson 1.1: Simple MySQL Connection Test")
print("=" * 45)

try:
    # Database connection
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'password here',
        database = 'learning_db'
    )

    if connection.is_connected():
        print("Successfully connected to MySQL")

        # Simple test query
        cursor = connection.cursor()
        cursor.execute("SELECT 'Hello from MySQL! as greeting")
        result = cursor.fetchone()
        print(f"Message from database: {result[0]}")
        
        # Close connection
        cursor.close()
        connection.close()
        print("Connection closed successfully")

except Exception as e:
    print(f"Conneciton failed: {e}")
    print("Check if MySQL server is running!")
    
    
print("\n Lesson 1.1 completed.")
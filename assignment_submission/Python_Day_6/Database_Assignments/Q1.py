import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""  # Leave blank if you haven't set a password
)
cursor = conn.cursor()

# 1. Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS TempDB")
cursor.execute("USE TempDB")

# 2. Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    grade INT
)
""")

# 3. Insert 5 student records
students = [
    ("Luffy", 85),
    ("Zoro", 78),
    ("Nami", 88),
    ("Sanji", 82),
    ("Usopp", 75)
]

cursor.executemany("INSERT INTO students (name, grade) VALUES (%s, %s)", students)

conn.commit()

print("Database, table, and student records created successfully.")

# Close connections
cursor.close()
conn.close()
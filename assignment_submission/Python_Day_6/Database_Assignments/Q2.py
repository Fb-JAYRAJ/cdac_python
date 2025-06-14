import mysql.connector

# Connect to MySQL and TempDB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # leave blank unless you have a password
    database="TempDB"
)
cursor = conn.cursor()

# Accept grade from user
grade_input = int(input("Enter grade to search for: "))

# Fetch students with that grade
query = "SELECT id, name, grade FROM students WHERE grade = %s"
cursor.execute(query, (grade_input,))
results = cursor.fetchall()

# Display results
if results:
    print(f"\nStudents with grade {grade_input}:")
    for student in results:
        print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}")
else:
    print(f"No students found with grade {grade_input}.")

# Close connection
cursor.close()
conn.close()
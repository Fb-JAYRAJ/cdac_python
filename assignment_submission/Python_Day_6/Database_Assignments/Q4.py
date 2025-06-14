import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="TempDB"
)

cursor = conn.cursor()

cursor.callproc("GetTopStudents")

for result in cursor.stored_results():
    students = result.fetchall()
    if students:
        print("\n🎓 Students with grade > 80:")
        for s in students:
            print(f"ID: {s[0]}, Name: {s[1]}, Grade: {s[2]}")
    else:
        print("No students found.")

cursor.close()
conn.close()
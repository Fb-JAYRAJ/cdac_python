import mysql.connector

# Connect to MySQL and TempDB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="TempDB"
)
cursor = conn.cursor()

# Create courses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100),
    teacher_name VARCHAR(100)
)
""")

# Function: Insert new course
def insert_course(course_name, teacher_name):
    query = "INSERT INTO courses (course_name, teacher_name) VALUES (%s, %s)"
    cursor.execute(query, (course_name, teacher_name))
    conn.commit()
    print("✅ Course inserted.")

# Function: Update teacher
def update_teacher(course_name, new_teacher):
    query = "UPDATE courses SET teacher_name = %s WHERE course_name = %s"
    cursor.execute(query, (new_teacher, course_name))
    conn.commit()
    print("✅ Teacher updated.")

# Function: Delete course by ID
def delete_course(course_id):
    query = "DELETE FROM courses WHERE id = %s"
    cursor.execute(query, (course_id,))
    conn.commit()
    print("Course deleted.")

def display_courses():
    cursor.execute("SELECT * FROM courses")
    results = cursor.fetchall()
    if results:
        print("\n📚 Courses:")
        for course in results:
            print(f"ID: {course[0]}, Name: {course[1]}, Teacher: {course[2]}")
    else:
        print("No courses found.")

while True:
    print("\n--- Course Menu ---")
    print("1. Insert Course")
    print("2. Update Teacher")
    print("3. Delete Course")
    print("4. Display All Courses")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter course name: ")
        teacher = input("Enter teacher name: ")
        insert_course(name, teacher)
    elif choice == "2":
        name = input("Enter course name to update: ")
        new_teacher = input("Enter new teacher name: ")
        update_teacher(name, new_teacher)
    elif choice == "3":
        cid = int(input("Enter course ID to delete: "))
        delete_course(cid)
    elif choice == "4":
        display_courses()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")

cursor.close()
conn.close()
import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="students",
            user="postgres",
            password="diabolist02",
            host="localhost",
            port="5432"
        )
        # print("Connected to the database")
        return conn
    except Exception as e:
        print(e)
        return None
    
connect_db()

def getAllStudents():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    records = cur.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Email: {row[3]}, Enrollment Date: {row[4]}")
    cur.close()
    conn.close()

def insertStudent(first_name, last_name, email, enrollment_date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date))
    conn.commit()
    cur.close()
    conn.close()

def updateStudentEmail(student_id, new_email):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()
    cur.close()
    conn.close()

def deleteStudent(student_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    cur.close()
    conn.close()

# Example usage
if __name__ == "__main__":
    getAllStudents()
    insertStudent('First', 'Last', 'email@example.com', '2023-09-03')
    updateStudentEmail(1, 'new.email@example.com')
    deleteStudent(1)
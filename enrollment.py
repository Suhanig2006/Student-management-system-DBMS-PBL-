from db_config import get_connection

def enroll_student(student_id, course_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO enrollment (student_id, course_id) VALUES (%s, %s)"
        cursor.execute(sql, (student_id, course_id))
        conn.commit()
        print("Student enrolled successfully.")
    except Exception as e:
        print(f"Error: {e}")
    cursor.close()
    conn.close()

def view_enrollments():
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT e.enrollment_id,
                    CONCAT(s.first_name,' ',s.last_name) AS student,
                    c.course_name, e.enrollment_date
             FROM enrollment e
             JOIN student s ON e.student_id = s.student_id
             JOIN course  c ON e.course_id  = c.course_id"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"\n{'EnrollID':<10} {'Student':<25} {'Course':<25} {'Date':<12}")
    print("-" * 72)
    for row in rows:
        print(f"{row[0]:<10} {row[1]:<25} {row[2]:<25} {str(row[3]):<12}")
    cursor.close()
    conn.close()

def view_student_courses(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT c.course_name, c.course_code, e.enrollment_date
             FROM enrollment e
             JOIN course c ON e.course_id = c.course_id
             WHERE e.student_id = %s"""
    cursor.execute(sql, (student_id,))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()
from db_config import get_connection

def add_course(course_name, course_code, credits, teacher_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO course (course_name, course_code, credits, teacher_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (course_name, course_code, credits, teacher_id))
    conn.commit()
    print(f"Course '{course_name}' added.")
    cursor.close()
    conn.close()

def view_all_courses():
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT c.course_id, c.course_name, c.course_code, c.credits,
                    CONCAT(t.first_name, ' ', t.last_name) AS teacher
             FROM course c
             LEFT JOIN teacher t ON c.teacher_id = t.teacher_id"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"\n{'ID':<5} {'Course Name':<25} {'Code':<12} {'Credits':<10} {'Teacher':<20}")
    print("-" * 72)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<25} {row[2]:<12} {row[3]:<10} {str(row[4]):<20}")
    cursor.close()
    conn.close()

def delete_course(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM course WHERE course_id=%s", (course_id,))
    conn.commit()
    print("Course deleted.")
    cursor.close()
    conn.close()
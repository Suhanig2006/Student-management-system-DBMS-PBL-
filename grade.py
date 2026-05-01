from db_config import get_connection

def calculate_grade(marks):
    if marks >= 90: return 'A+'
    elif marks >= 80: return 'A'
    elif marks >= 70: return 'B'
    elif marks >= 60: return 'C'
    elif marks >= 50: return 'D'
    else: return 'F'

def add_grade(enrollment_id, marks, exam_date):
    conn = get_connection()
    cursor = conn.cursor()
    grade = calculate_grade(marks)
    sql = "INSERT INTO grade (enrollment_id, marks, grade, exam_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (enrollment_id, marks, grade, exam_date))
    conn.commit()
    print(f"Grade '{grade}' added for marks {marks}.")
    cursor.close()
    conn.close()

def view_grades():
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT g.grade_id,
                    CONCAT(s.first_name,' ',s.last_name) AS student,
                    c.course_name, g.marks, g.grade, g.exam_date
             FROM grade g
             JOIN enrollment e ON g.enrollment_id = e.enrollment_id
             JOIN student s    ON e.student_id     = s.student_id
             JOIN course  c    ON e.course_id      = c.course_id"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"\n{'GradeID':<10} {'Student':<25} {'Course':<25} {'Marks':<8} {'Grade':<6} {'Date':<12}")
    print("-" * 86)
    for row in rows:
        print(f"{row[0]:<10} {row[1]:<25} {row[2]:<25} {row[3]:<8} {row[4]:<6} {str(row[5]):<12}")
    cursor.close()
    conn.close()

def student_report(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT c.course_name, g.marks, g.grade
             FROM grade g
             JOIN enrollment e ON g.enrollment_id = e.enrollment_id
             JOIN course c     ON e.course_id      = c.course_id
             WHERE e.student_id = %s"""
    cursor.execute(sql, (student_id,))
    rows = cursor.fetchall()
    print(f"\n{'Course':<30} {'Marks':<10} {'Grade'}")
    print("-" * 50)
    total = 0
    for row in rows:
        print(f"{row[0]:<30} {row[1]:<10} {row[2]}")
        total += row[1]
    if rows:
        print(f"\nAverage: {total/len(rows):.2f}")
    cursor.close()
    conn.close()
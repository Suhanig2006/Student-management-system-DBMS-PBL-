from db_config import get_connection

def add_student(first_name, last_name, email, phone, dob, address, dept_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO student
             (first_name, last_name, email, phone, dob, address, dept_id)
             VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql, (first_name, last_name, email, phone, dob, address, dept_id))
    conn.commit()
    print(f"Student '{first_name} {last_name}' added.")
    cursor.close()
    conn.close()

def view_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT s.student_id, s.first_name, s.last_name,
                    s.email, s.phone, d.dept_name
             FROM student s
             LEFT JOIN department d ON s.dept_id = d.dept_id"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"\n{'ID':<5} {'First':<15} {'Last':<15} {'Email':<28} {'Phone':<14} {'Dept'}")
    print("-" * 90)
    for r in rows:
        print(f"{r[0]:<5} {r[1]:<15} {r[2]:<15} {r[3]:<28} {str(r[4]):<14} {str(r[5])}")
    cursor.close()
    conn.close()

def update_student(student_id, phone=None, address=None, dept_id=None):
    conn = get_connection()
    cursor = conn.cursor()
    if phone:
        cursor.execute("UPDATE student SET phone=%s WHERE student_id=%s", (phone, student_id))
    if address:
        cursor.execute("UPDATE student SET address=%s WHERE student_id=%s", (address, student_id))
    if dept_id:
        cursor.execute("UPDATE student SET dept_id=%s WHERE student_id=%s", (dept_id, student_id))
    conn.commit()
    print("Student updated.")
    cursor.close()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE student_id=%s", (student_id,))
    conn.commit()
    print("Student deleted.")
    cursor.close()
    conn.close()

def search_student(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    like = f"%{keyword}%"
    sql = """SELECT s.student_id, s.first_name, s.last_name,
                    s.email, d.dept_name
             FROM student s
             LEFT JOIN department d ON s.dept_id = d.dept_id
             WHERE CAST(s.student_id AS CHAR) LIKE %s
                OR s.first_name LIKE %s
                OR s.last_name LIKE %s
                OR s.email LIKE %s"""
    cursor.execute(sql, (like, like, like, like))
    rows = cursor.fetchall()
    if rows:
        print(f"\n{'ID':<5} {'First':<15} {'Last':<15} {'Email':<28} {'Dept'}")
        print("-" * 70)
        for r in rows:
            print(f"{r[0]:<5} {r[1]:<15} {r[2]:<15} {r[3]:<28} {str(r[4])}")
    else:
        print("No student found matching your search.")
    cursor.close()
    conn.close()
from db_config import get_connection

def add_department(dept_name, dept_code, hod_name, location):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO department (dept_name, dept_code, hod_name, location)
             VALUES (%s, %s, %s, %s)"""
    cursor.execute(sql, (dept_name, dept_code, hod_name, location))
    conn.commit()
    print(f"Department '{dept_name}' added.")
    cursor.close()
    conn.close()

def view_all_departments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM department")
    rows = cursor.fetchall()
    print(f"\n{'ID':<5} {'Name':<25} {'Code':<10} {'HOD':<25} {'Location':<20}")
    print("-" * 85)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<25} {row[2]:<10} {str(row[3]):<25} {str(row[4]):<20}")
    cursor.close()
    conn.close()

def update_department(dept_id, hod_name=None, location=None):
    conn = get_connection()
    cursor = conn.cursor()
    if hod_name:
        cursor.execute("UPDATE department SET hod_name=%s WHERE dept_id=%s", (hod_name, dept_id))
    if location:
        cursor.execute("UPDATE department SET location=%s WHERE dept_id=%s", (location, dept_id))
    conn.commit()
    print("Department updated.")
    cursor.close()
    conn.close()

def delete_department(dept_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM department WHERE dept_id=%s", (dept_id,))
    conn.commit()
    print("Department deleted.")
    cursor.close()
    conn.close()

def view_department_students(dept_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT s.student_id, CONCAT(s.first_name,' ',s.last_name) AS name, s.email
             FROM student s WHERE s.dept_id = %s"""
    cursor.execute(sql, (dept_id,))
    rows = cursor.fetchall()
    print(f"\n{'ID':<6} {'Name':<30} {'Email'}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<6} {row[1]:<30} {row[2]}")
    cursor.close()
    conn.close()
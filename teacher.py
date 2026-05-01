from db_config import get_connection

def add_teacher(first_name, last_name, email, subject):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO teacher (first_name, last_name, email, subject) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (first_name, last_name, email, subject))
    conn.commit()
    print(f"Teacher '{first_name} {last_name}' added.")
    cursor.close()
    conn.close()

def view_all_teachers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teacher")
    rows = cursor.fetchall()
    print(f"\n{'ID':<5} {'First':<15} {'Last':<15} {'Email':<30} {'Subject':<20}")
    print("-" * 85)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<30} {row[4]:<20}")
    cursor.close()
    conn.close()

def delete_teacher(teacher_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM teacher WHERE teacher_id=%s", (teacher_id,))
    conn.commit()
    print("Teacher deleted.")
    cursor.close()
    conn.close()
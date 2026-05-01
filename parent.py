from db_config import get_connection

def add_parent(student_id, father_name, mother_name,
               father_phone, mother_phone,
               father_occ, mother_occ, emergency):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO parent_details
             (student_id, father_name, mother_name,
              father_phone, mother_phone,
              father_occupation, mother_occupation, emergency_contact)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql, (student_id, father_name, mother_name,
                         father_phone, mother_phone,
                         father_occ, mother_occ, emergency))
    conn.commit()
    print("Parent details added.")
    cursor.close()
    conn.close()

def view_parent(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT p.*, CONCAT(s.first_name,' ',s.last_name) AS student_name
             FROM parent_details p
             JOIN student s ON p.student_id = s.student_id
             WHERE p.student_id = %s"""
    cursor.execute(sql, (student_id,))
    row = cursor.fetchone()
    if row:
        print(f"\n--- Parent Details for {row[-1]} ---")
        print(f"Father : {row[2]}  |  Phone: {row[4]}  |  Occupation: {row[6]}")
        print(f"Mother : {row[3]}  |  Phone: {row[5]}  |  Occupation: {row[7]}")
        print(f"Emergency Contact: {row[8]}")
    else:
        print("No parent record found for this student.")
    cursor.close()
    conn.close()

def update_parent(student_id, emergency_contact=None, father_phone=None, mother_phone=None):
    conn = get_connection()
    cursor = conn.cursor()
    if emergency_contact:
        cursor.execute("UPDATE parent_details SET emergency_contact=%s WHERE student_id=%s",
                       (emergency_contact, student_id))
    if father_phone:
        cursor.execute("UPDATE parent_details SET father_phone=%s WHERE student_id=%s",
                       (father_phone, student_id))
    if mother_phone:
        cursor.execute("UPDATE parent_details SET mother_phone=%s WHERE student_id=%s",
                       (mother_phone, student_id))
    conn.commit()
    print("Parent details updated.")
    cursor.close()
    conn.close()

def view_all_parents():
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT CONCAT(s.first_name,' ',s.last_name) AS student,
                    p.father_name, p.father_phone,
                    p.mother_name, p.mother_phone,
                    p.emergency_contact
             FROM parent_details p
             JOIN student s ON p.student_id = s.student_id"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"\n{'Student':<22} {'Father':<18} {'F.Phone':<14} {'Mother':<18} {'M.Phone':<14} {'Emergency'}")
    print("-" * 100)
    for r in rows:
        print(f"{r[0]:<22} {r[1]:<18} {r[2]:<14} {r[3]:<18} {r[4]:<14} {r[5]}")
    cursor.close()
    conn.close()
from db_config import get_connection

def add_slot(course_id, teacher_id, day, start_time, end_time, room):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO timetable (course_id, teacher_id, day_of_week,
                                    start_time, end_time, room_number)
             VALUES (%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql, (course_id, teacher_id, day, start_time, end_time, room))
    conn.commit()
    print(f"Timetable slot added: {day} {start_time}-{end_time} in Room {room}.")
    cursor.close()
    conn.close()

def view_full_timetable():
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT t.day_of_week, t.start_time, t.end_time,
                    c.course_name, c.course_code,
                    CONCAT(te.first_name,' ',te.last_name) AS teacher,
                    t.room_number
             FROM timetable t
             JOIN course  c  ON t.course_id  = c.course_id
             JOIN teacher te ON t.teacher_id = te.teacher_id
             ORDER BY FIELD(t.day_of_week,
               'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'),
               t.start_time"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"\n{'Day':<12} {'Time':<16} {'Course':<25} {'Code':<10} {'Teacher':<22} {'Room'}")
    print("-" * 95)
    for r in rows:
        time_range = f"{str(r[1])[:5]}-{str(r[2])[:5]}"
        print(f"{r[0]:<12} {time_range:<16} {r[3]:<25} {r[4]:<10} {r[5]:<22} {r[6]}")
    cursor.close()
    conn.close()

def view_teacher_timetable(teacher_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT t.day_of_week, t.start_time, t.end_time,
                    c.course_name, t.room_number
             FROM timetable t
             JOIN course c ON t.course_id = c.course_id
             WHERE t.teacher_id = %s
             ORDER BY FIELD(t.day_of_week,
               'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'),
               t.start_time"""
    cursor.execute(sql, (teacher_id,))
    rows = cursor.fetchall()
    print(f"\n{'Day':<12} {'Time':<16} {'Course':<25} {'Room'}")
    print("-" * 60)
    for r in rows:
        time_range = f"{str(r[1])[:5]}-{str(r[2])[:5]}"
        print(f"{r[0]:<12} {time_range:<16} {r[2]:<25} {r[4]}")
    cursor.close()
    conn.close()

def view_course_timetable(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """SELECT day_of_week, start_time, end_time, room_number
             FROM timetable WHERE course_id = %s
             ORDER BY FIELD(day_of_week,
               'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'),
               start_time"""
    cursor.execute(sql, (course_id,))
    for r in cursor.fetchall():
        print(f"{r[0]}  {str(r[1])[:5]}-{str(r[2])[:5]}  Room: {r[3]}")
    cursor.close()
    conn.close()

def delete_slot(slot_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM timetable WHERE slot_id=%s", (slot_id,))
    conn.commit()
    print("Slot deleted.")
    cursor.close()
    conn.close()
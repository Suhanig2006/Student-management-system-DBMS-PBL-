from department import add_department, view_all_departments, update_department, delete_department, view_department_students
from student    import add_student, view_all_students, update_student, delete_student, search_student
from parent     import add_parent, view_parent, update_parent, view_all_parents
from teacher    import add_teacher, view_all_teachers, delete_teacher
from course     import add_course, view_all_courses, delete_course
from timetable  import add_slot, view_full_timetable, view_teacher_timetable, view_course_timetable, delete_slot
from enrollment import enroll_student, view_enrollments, view_student_courses
from grade      import add_grade, view_grades, student_report

def main_menu():
    while True:
        print("\n======== Student Management System ========")
        print("1. Department    2. Student      3. Parent Details")
        print("4. Teacher       5. Course       6. Timetable")
        print("7. Enrollment    8. Grades       9. Exit")
        choice = input("Enter choice: ").strip()
        menu_map = {
            '1': dept_menu, '2': student_menu, '3': parent_menu,
            '4': teacher_menu, '5': course_menu, '6': timetable_menu,
            '7': enrollment_menu, '8': grade_menu
        }
        if choice == '9':
            print("Goodbye!")
            break
        elif choice in menu_map:
            menu_map[choice]()
        else:
            print("Invalid choice.")

def dept_menu():
    print("\n--- Department ---")
    print("1.Add  2.View All  3.Update  4.Delete  5.View Students in Dept")
    c = input("Choice: ")
    if c == '1':
        add_department(input("Dept name: "), input("Dept code: "),
                       input("HOD name: "), input("Location: "))
    elif c == '2': view_all_departments()
    elif c == '3':
        did = int(input("Dept ID: "))
        update_department(did,
                          input("New HOD (Enter to skip): ") or None,
                          input("New location (Enter to skip): ") or None)
    elif c == '4': delete_department(int(input("Dept ID: ")))
    elif c == '5': view_department_students(int(input("Dept ID: ")))

def student_menu():
    print("\n--- Student ---")
    print("1.Add  2.View All  3.Update  4.Delete  5.Search")
    c = input("Choice: ")
    if c == '1':
        add_student(input("First: "), input("Last: "), input("Email: "),
                    input("Phone: "), input("DOB (YYYY-MM-DD): "),
                    input("Address: "), int(input("Dept ID: ")))
    elif c == '2': view_all_students()
    elif c == '3':
        sid = int(input("Student ID: "))
        update_student(sid,
                       input("New phone (Enter to skip): ") or None,
                       input("New address (Enter to skip): ") or None,
                       input("New dept ID (Enter to skip): ") or None)
    elif c == '4': delete_student(int(input("Student ID: ")))
    elif c == '5': search_student(input("Keyword: "))

def parent_menu():
    print("\n--- Parent Details ---")
    print("1.Add  2.View by Student  3.View All  4.Update")
    c = input("Choice: ")
    if c == '1':
        add_parent(int(input("Student ID: ")),
                   input("Father name: "), input("Mother name: "),
                   input("Father phone: "), input("Mother phone: "),
                   input("Father occupation: "), input("Mother occupation: "),
                   input("Emergency contact: "))
    elif c == '2': view_parent(int(input("Student ID: ")))
    elif c == '3': view_all_parents()
    elif c == '4':
        sid = int(input("Student ID: "))
        update_parent(sid,
                      input("New emergency contact (Enter to skip): ") or None,
                      input("New father phone (Enter to skip): ") or None,
                      input("New mother phone (Enter to skip): ") or None)

def teacher_menu():
    print("\n--- Teacher ---")
    print("1.Add  2.View All  3.Delete")
    c = input("Choice: ")
    if c == '1':
        add_teacher(input("First: "), input("Last: "),
                    input("Email: "), input("Subject: "))
    elif c == '2': view_all_teachers()
    elif c == '3': delete_teacher(int(input("Teacher ID: ")))

def course_menu():
    print("\n--- Course ---")
    print("1.Add  2.View All  3.Delete")
    c = input("Choice: ")
    if c == '1':
        add_course(input("Course name: "), input("Course code: "),
                   int(input("Credits: ")), int(input("Teacher ID: ")))
    elif c == '2': view_all_courses()
    elif c == '3': delete_course(int(input("Course ID: ")))

def timetable_menu():
    print("\n--- Timetable ---")
    print("1.Add Slot  2.View Full Timetable  3.Teacher Schedule  4.Course Schedule  5.Delete Slot")
    c = input("Choice: ")
    if c == '1':
        add_slot(int(input("Course ID: ")), int(input("Teacher ID: ")),
                 input("Day (e.g. Monday): "),
                 input("Start time (HH:MM): "), input("End time (HH:MM): "),
                 input("Room number: "))
    elif c == '2': view_full_timetable()
    elif c == '3':
        tid = input("Teacher ID: ")
        if tid:
            view_teacher_timetable(int(tid))
        else:
            print("Teacher ID cannot be empty.")
    elif c == '4': view_course_timetable(int(input("Course ID: ")))
    elif c == '5': delete_slot(int(input("Slot ID: ")))

def enrollment_menu():
    print("\n--- Enrollment ---")
    print("1.Enroll  2.View All  3.Student Courses")
    c = input("Choice: ")
    if c == '1':
        enroll_student(int(input("Student ID: ")), int(input("Course ID: ")))
    elif c == '2': view_enrollments()
    elif c == '3': view_student_courses(int(input("Student ID: ")))

def grade_menu():
    print("\n--- Grades ---")
    print("1.Add Grade  2.View All  3.Student Report")
    c = input("Choice: ")
    if c == '1':
        add_grade(int(input("Enrollment ID: ")),
                  float(input("Marks (0-100): ")),
                  input("Exam date (YYYY-MM-DD): "))
    elif c == '2': view_grades()
    elif c == '3': student_report(int(input("Student ID: ")))

if __name__ == "__main__":
    main_menu()
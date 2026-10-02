students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    department = input("Enter department: ")

    student = [roll_no, name, department]
    students.append(student)

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\nStudent Details")

        for student in students:
            print("Roll No:", student[0])
            print("Name:", student[1])
            print("Department:", student[2])
            print("----------------")


def search_student():
    roll_no = input("Enter roll number: ")

    for student in students:
        if student[0] == roll_no:
            print("\nStudent Found!")
            print("Roll No:", student[0])
            print("Name:", student[1])
            print("Department:", student[2])
            return

    print("Student not found.")


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
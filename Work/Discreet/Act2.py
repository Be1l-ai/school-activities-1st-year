student = {}

def add_student(name, id):
    student[id] = {"student":name, "grade":{"prelim": 0, "midterm": 0, "final": 0}}
    return f"Student {name} added successfully"
    
def add_grade(id, pre, mid, fin):
    if id in student:
        student[id]["grade"] = {"prelim": pre, "midterm": mid, "final": fin}
        return "Grade added successfully"
    else:
        return "Student not found"

def calculate(id):
    if id in student:
        sum = student[id]["grade"]["prelim"] + student[id]["grade"]["midterm"] + student[id]["grade"]["final"]
        average = sum / len(student[id]["grade"])
        return average
    else:
        return "student not found"
    
def show_add_student():
    id = input("Enter student ID: ")
    if id in student:
        if input("Student already exists would you like to update the student information? (yes/no) ") == "yes":
            action = input("Would you like to update name or id? (name/id) ")
            if action.lower() == "name":
                new_name = input("Enter new name: ")
                student[id]["student"] = new_name
            elif action.lower() == "id":
                new_id = input("Enter new ID: ")
                student[new_id] = student.pop(id)
            return "Student information updated successfully."
        else:
            print("Student already exists:", student[id]["student"])
    else:
        name = input("Enter student name: ")
    
        print(add_student(name, id))
    
def show_add_grade():
    id = input("Enter student ID: ")
    if id not in student:
        print("Student Not found")
    else:
        grade_prelim = float(input("Enter prelim grade: "))
        grade_midterm = float(input("Enter midterm grade: "))
        grade_final = float(input("Enter final grade: "))

        print(add_grade(id, grade_prelim, grade_midterm, grade_final))

def show_calculate_student():
    id = input("Enter student ID: ")
    if id not in student:
        print("Student Not found")
    else:
        print(f"Student {student[id]['student']} Average grade is:", calculate(id))
    
def remove_student(id):
    if id in student:
        del student[id]
        return f"Student with ID {id} removed successfully."
    else:
        return "Student not found."

def get_class_average():
    if not student:
        print("No grades found to calculate the average.")
        return
    all_grades = []
    for stud in student.values():
        all_grades.extend(stud["grade"].values())
    class_average = sum(int(grade) for grade in all_grades) / len(all_grades)
    print(f"The overall class average is: {class_average:.2f}")

def rank_student():
    all_grades = []
    for stud in student.values():
        all_grades.extend(stud["grade"].values())
    all_grades = [int(grade) for grade in all_grades]
    if not all_grades:
        print("No grades available to rank students.")
        return
    ranked_students = sorted(student.items(), key=lambda x: sum(x[1]["grade"].values()) / len(x[1]["grade"]), reverse=True)
    print("\n--- Student Ranking ---")
    for i, (id, info) in enumerate(ranked_students, start=1):
        average = sum(info["grade"].values()) / len(info["grade"])
        print(f"{i}. {info['student']} (ID: {id}) - Average: {average:.2f}")

def find_failing_student():
    all_grades = []
    for stud in student.values():
        all_grades.extend(stud["grade"].values())
    all_grades = [int(grade) for grade in all_grades]
    if not all_grades:
        print("No grades available to find failing students.")
        return
    failing_students = [id for id, info in student.items() if any(grade < 75 for grade in info["grade"].values())]
    if not failing_students:
        print("No failing students found.")
    else:
        print("Failing students:")
        for id in failing_students:
            print(f" - {student[id]['student']} (ID: {id})")

def show():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add/Update Student")
        print("2. Add/Update Grade")
        print("3. Calculate")
        print("4. Remove a student")
        print("5. Show all student")
        print("6. Rank Students by Average")
        print("7. Find failing students")
        print("8. Exit")
        action = input("Enter your choice: ")
        if action == "1":
            show_add_student()
        elif action == "2":
            show_add_grade()
        elif action == "3":
            action2 = input("Calculate [1] Student Average or [2] Class Average")
            if action2 == "1":
                show_calculate_student()
            else:
                get_class_average()
        elif action == "4":
            id = input("Enter student ID to remove: ")
            print(remove_student(id))
        elif action == "5":
            if len(student) == 0:
                print("No student")
            else:
                print(student)
        elif action == "6":
            rank_student()
        elif action == "7":
            find_failing_student()
        elif action == "8":
            break
        else:
            print("Invalid action. Please try again.")
            continue
        
    
show()
        
    

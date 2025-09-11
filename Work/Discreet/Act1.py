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
        print("Student already exists:", student[id]["student"])
        return
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

def show_calculate():
    id = input("Enter student ID: ")
    if id not in student:
        print("Student Not found")
    else:
        print(f"Student {student[id]['student']} Average grade is:", calculate(id))
    
def show():
    while True:
        action = input("Choose an action: (1) Add Student, (2) Add Grade, (3) Calculate Average, (4) Show All Student, (5) Exit: ")
        if action == "1":
            show_add_student()
        elif action == "2":
            show_add_grade()
        elif action == "3":
            show_calculate()
        elif action == "4":
            if len(student) == 0:
                print("No student")
            else:
                print(student)
        elif action == "5":
            break
        else:
            print("Invalid action. Please try again.")
            continue
        
    
show()
        
    

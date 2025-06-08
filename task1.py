student_marks={
    "Ajay":95,
    "Alice":85,
    "Rahul":90,
    "Harsh":88,
    "Rohit":87
}

name = input("Enter the student's name: ")
if name in student_marks:
    print(f"{name}'s marks is : {student_marks[name]}")
else:
    print("Student not found.")

student_marks = {
    "Amit": 85,
    "Sneha": 92,
    "Ravi": 78,
    "Priya": 88,
    "Karan": 95
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the record.")
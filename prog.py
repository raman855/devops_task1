# List of students and their grades
students_grades = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 78},
    {"name": "Charlie", "grade": 92},
    {"name": "David", "grade": 88},
    {"name": "Eva", "grade": 76}
]

# Calculate the average grade
total_grades = sum(student["grade"] for student in students_grades)
average_grade = total_grades / len(students_grades)

# Write the result to a text file
with open("average_grade.txt", "w") as file:
    file.write(f"Average Grade: {average_grade:.2f}\n")
    file.write("Student Grades:\n")
    for student in students_grades:
        file.write(f"{student['name']}: {student['grade']}\n")

print("Average grade calculated and written to 'average_grade.txt'")

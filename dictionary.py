# dictionary.py
student = {
    "name": "Alex Mercer",
    "age": 21,
    "course": "Computer Science",
    "grade": "A"
}
print(f"Original Student details: {student}")

student_name = student["name"]
print(f"Accessed Name: {student_name}")

student["grade"] = "A+"
student["age"] = 22  
print(f"Updated Student details: {student}")

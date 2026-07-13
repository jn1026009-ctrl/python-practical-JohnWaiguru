# class_variables.py
class Student:
    school_name = "Zetech University"

    def __init__(self, name, admission_number):
        self.name = name
        self.admission_number = admission_number

    def display_details(self):
        print(f"Name: {self.name} | Admin No: {self.admission_number} | School: {self.school_name}")

student1 = Student("Alex", "CS-101")
student2 = Student("Brian", "CS-102")

print("--- Accessing Class Variable ---")
student1.display_details()
student2.display_details()

print("\nUpdating class variable for the entire class...")
# Modifying class variable globally
Student.school_name = "Tech Institute of East Africa"
student1.display_details()
student2.display_details()

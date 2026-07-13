# classes.py
class Student:
    def __init__(self, name, admin_number, course):
        self.name = name
        self.admin_number = admin_number
        self.course = course

    def display_info(self):
        print(f"Student Name: {self.name} | Admin No: {self.admin_number} | Course: {self.course}")

student1 = Student("Henry Steph", "CIT-01-0021/2026", "Computer Science")
student2 = Student("Mercy Aluel", "CIT-01-0022/2026", "Software Engineering")
student3 = Student("Kibet Collins", "CIT-01-0023/2026", "Cyber Security")

print("--- Student Directory ---")
student1.display_info()
student2.display_info()
student3.display_info()

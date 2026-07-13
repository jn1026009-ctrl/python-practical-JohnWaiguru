# class_methods.py
class University:
    university_name = "Zetech University"

    def __init__(self, course_name, duration_years):
        self.course_name = course_name
        self.duration_years = duration_years

    @classmethod
    def update_university_name(cls, new_name):
        cls.university_name = new_name

    def display_program_info(self):
        print(f"Course: {self.course_name} | Duration: {self.duration_years} Years | University: {self.university_name}")

prog1 = University("Business Administration", 3)
prog2 = University("Software Engineering", 4)

print("--- Before Updating Class Variable ---")
prog1.display_program_info()
prog2.display_program_info()

University.update_university_name("Zetech National University")

print("\n--- After Class Method Update ---")
prog1.display_program_info()
prog2.display_program_info()

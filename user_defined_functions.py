# user_defined_functions.py
def add_numbers(a, b):
    return a + b

def area_of_rectangle(length, width):
    return length * width

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def display_student_details(name, admin_no, course):
    print(f"--- Student Record ---")
    print(f"Name: {name}")
    print(f"Admission No: {admin_no}")
    print(f"Course: {course}")
    print("-" * 22)

print(f"Sum of 5 and 7: {add_numbers(5, 7)}")
print(f"Area of 10x5 rectangle: {area_of_rectangle(10, 5)}")
print(f"Is 17 prime?: {is_prime(17)}")
print(f"Factorial of 5: {factorial(5)}")
display_student_details("John Doe", "CS/001/2026", "Information Technology")

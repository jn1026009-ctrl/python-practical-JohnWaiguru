# lambda_functions.py
add = lambda x, y: x + y
print(f"Lambda Addition (10 + 5): {add(10, 5)}")

multiply = lambda x, y: x * y
print(f"Lambda Multiplication (4 * 5): {multiply(4, 5)}")

students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_students = sorted(students, key=lambda student: student[1])
print(f"Sorted students by age: {sorted_students}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filtered Even numbers: {even_numbers}")

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Mapped Squared numbers: {squared_numbers}")

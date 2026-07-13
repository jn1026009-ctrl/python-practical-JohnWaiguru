# builtin_functions.py
numbers = [-5, 10, 3, 22, -15, 8]
sentence = "Hello Python"

print(f"1. Length of numbers list: {len(numbers)}")
print(f"2. Maximum value in numbers: {max(numbers)}")
print(f"3. Minimum value in numbers: {min(numbers)}")
print(f"4. Sum of numbers: {sum(numbers)}")
print(f"5. Type of 'sentence' variable: {type(sentence)}")
print(f"6. Sorted numbers: {sorted(numbers)}")
print(f"7. Absolute value of -15: {abs(-15)}")
print(f"8. Round 3.14159 to 2 decimal places: {round(3.14159, 2)}")

print("9. Demonstration of input():")
user_name = input("   Please enter your name: ")
print(f"10. Demonstration of print(): Welcome, {user_name}!")

# selection.py
score = 65
print(f"--- Student Score Evaluation (Score: {score}) ---")
if score >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
print("-" * 40 + "\n")

print("--- Even or Odd Check ---")
user_input = input("Enter an integer to check if it's even or odd: ")
try:
    num = int(user_input)
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")
except ValueError:
    print("Invalid input! Please run the program again and enter an integer.")
print("-" * 40 + "\n")

print("--- Finding the Largest of Three Numbers ---")
num1, num2, num3 = 14, 27, 19
print(f"Numbers to compare: {num1}, {num2}, {num3}")

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")

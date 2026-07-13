# looping.py
print("--- Numbers 1 to 20 ---")
for i in range(1, 21):
    print(i, end=" ")
print("\n\n" + "-" * 40 + "\n")

print("--- Multiplication Table ---")
user_input = input("Enter a number to get its multiplication table: ")
try:
    number = int(user_input)
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
except ValueError:
    print("Invalid numeric entry.")
print("-" * 40 + "\n")

print("--- Sum of Numbers 1 to 100 ---")
total_sum = 0
counter = 1
while counter <= 100:
    total_sum += counter
    counter += 1
print(f"The sum of numbers from 1 to 100 is: {total_sum}")
print("-" * 40 + "\n")

print("--- Even Numbers between 1 and 50 ---")
for even_num in range(1, 51):
    if even_num % 2 == 0:
        print(even_num, end=" ")
print()

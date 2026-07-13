# string.py
first_name = "Jane"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Concatenated Name: {full_name}")

sample_str = "Python Programming"
print(f"Character at index 0: {sample_str[0]}")
print(f"Sliced string (indices 0 to 6): '{sample_str[0:6]}'")

print(f"Uppercase: {sample_str.upper()}")
print(f"Lowercase: {sample_str.lower()}")
print(f"Replace 'Python' with 'Java': {sample_str.replace('Python', 'Java')}")
print(f"Split string by space: {sample_str.split(' ')}")

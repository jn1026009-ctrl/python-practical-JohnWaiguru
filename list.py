# list.py
fruits = ["apple", "banana", "cherry"]
print(f"Original list: {fruits}")

fruits.append("orange")
print(f"After adding orange: {fruits}")

fruits.remove("banana")
print(f"After removing banana: {fruits}")

fruits[1] = "blueberry" 
print(f"After updating index 1: {fruits}\n")

print("Iterating through fruits:")
for fruit in fruits:
    print(f"- {fruit}")

# tuple.py
coordinates = (10, 20, 30)
print(f"Coordinates tuple: {coordinates}")
print(f"Element at index 0: {coordinates[0]}")

print("Attempting to modify the tuple...")
try:
    coordinates[0] = 99
except TypeError as e:
    print(f"Error caught successfully: {e}")
    print("Explanation: Tuples are immutable sequence types in Python. Once defined, their elements cannot be changed.")

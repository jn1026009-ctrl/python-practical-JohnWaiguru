# set.py
numbers_set = {1, 2, 2, 3, 4, 4, 4, 5}
print(f"Set elements: {numbers_set}")
print("Notice how duplicate elements (2 and 4) were automatically removed!\n")

numbers_set.add(6)
print(f"After adding 6: {numbers_set}")

numbers_set.remove(3)
print(f"After removing 3: {numbers_set}")

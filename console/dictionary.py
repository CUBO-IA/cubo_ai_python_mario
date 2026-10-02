"""
DICTIONARY (dict) — key/value mappings
Run: python dictionary.py
Dictionaries preserve insertion order. Keys must be hashable; values can be any type.
"""

# 1. Creating dictionaries
student = {"name": "Lina", "age": 18, "active": True}
empty = {}
print(student, type(student))

# 2. Read, add, update, delete
print(student["name"])
print(student.get("grade", "Not provided"))  # default avoids KeyError
student["grade"] = 10
student["age"] = 19
del student["active"]
print(student)

# 3. Membership checks keys, not values
print("name" in student)
print("Lina" in student.values())

# 4. Iterate through keys, values, or pairs
for key in student:
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(key, "=", value)

# 5. Useful methods
student.update({"city": "San Salvador", "age": 20})
removed = student.pop("grade")
print(student, removed)
print(student.keys(), student.values(), student.items())

# 6. Nested dictionaries
grades = {
    "Ana": {"math": 9, "python": 10},
    "Luis": {"math": 8, "python": 9},
}
print(grades["Ana"]["python"])

# 7. Dictionary comprehension
squares = {n: n * n for n in range(1, 6)}
print(squares)

# EXERCISES
# 1. Create a profile dictionary with name, age, and favorite_language.
# 2. Update the age and add a country.
# 3. Print each key and value using .items().
# 4. Count the frequency of letters in a word using a dictionary.

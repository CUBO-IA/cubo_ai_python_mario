"""
NONETYPE (NoneType) — the type of None
Run: python nonetype.py
None represents the absence of a value or a deliberate "no result".
"""

# 1. None is a singleton value
result = None
print(result, type(result))  # <class 'NoneType'>

# 2. Functions return None if no return statement is used.
def greet(name):
    print(f"Hello, {name}")

returned = greet("Sam")
print("Returned:", returned)

# 3. Use `is None` to check for None.
value = None
if value is None:
    print("No value has been supplied.")

# 4. None is different from 0, False, and an empty string.
print(None == 0, None == False, None == "")

# 5. None can be a default or a marker for optional information.
def describe(value=None):
    if value is None:
        return "Nothing to describe"
    return f"Value: {value}"

print(describe(), describe(0))

# EXERCISES
# 1. Create a variable with None and print its type.
# 2. Write a function that returns None when given an empty string.
# 3. Check a variable using `is None`.
# 4. Explain why None, False, and 0 should not be treated as identical.

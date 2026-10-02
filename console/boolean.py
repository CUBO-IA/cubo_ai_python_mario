"""
BOOLEAN (bool) — True and False
Run: python boolean.py

A boolean represents one of two logical values: True or False.
Python uses booleans in decisions, comparisons, and loops.
"""

# 1. The two boolean values (capitalization matters)
is_learning = True
has_finished = False
print(is_learning, type(is_learning))
print(has_finished, type(has_finished))

# 2. Comparisons produce booleans
print(5 > 3)       # True
print(5 == 3)      # False
print(5 != 3)      # True
print("cat" == "cat")

# 3. Logical operators
age = 18
has_id = True
print(age >= 18 and has_id)  # both conditions must be true
print(age < 18 or has_id)    # at least one condition must be true
print(not has_id)            # reverses a boolean

# 4. Truthiness: values that behave like True or False in conditions
# Empty values and numeric zero are generally falsey; non-empty values are truthy.
for value in [0, 1, "", "hello", [], [0], None]:
    print(repr(value), "->", bool(value))

# 5. Use booleans in control flow
if age >= 18:
    print("Adult")
else:
    print("Not an adult")

# Common mistake: = assigns; == compares.
# is_ready = True   # assignment
# is_ready == True  # comparison; often simply write: if is_ready:

# EXERCISES
# 1. Create a boolean called is_sunny.
# 2. Print whether 27 is between 18 and 30 (inclusive).
# 3. Given password_ok and account_active booleans, require both to be true.
# 4. Test bool() on 0, -1, "0", and an empty dictionary.

"""
INTEGER (int) — whole numbers
Run: python integer.py
Integers are whole numbers, positive, negative, or zero.
"""

# 1. Creating integers
students = 25
temperature = -4
zero = 0
print(students, type(students))

# 2. Arithmetic
print(7 + 3)    # addition: 10
print(7 - 3)    # subtraction: 4
print(7 * 3)    # multiplication: 21
print(7 / 3)    # division: float result
print(7 // 3)   # floor division: 2
print(7 % 3)    # remainder: 1
print(7 ** 3)   # exponentiation: 343

# 3. Order of operations and parentheses
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20

# 4. Conversion (casting)
print(int("42"))
print(int(3.9))       # truncates toward zero, does not round
# int("3.9") raises ValueError; parse as float first if needed.

# 5. Useful built-ins
print(abs(-12), pow(2, 5), min(2, 8), max(2, 8))
print(divmod(17, 5))  # (quotient, remainder)

# 6. Integers can be very large
huge = 10 ** 100
print(huge)

# 7. Updating a variable
score = 10
score += 5
score *= 2
print(score)

# EXERCISES
# 1. Calculate the number of minutes in 3 days.
# 2. Find quotient and remainder when 97 is divided by 8.
# 3. Convert the string "2026" to an integer and add 1.
# 4. Explain the difference between / and // using your own examples.

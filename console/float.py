"""
FLOAT (float) — numbers with a fractional part
Run: python float.py
Floats represent approximate real-number values using binary floating point.
"""

# 1. Creating floats
price = 12.50
ratio = 0.75
negative = -2.4
print(price, type(price))

# 2. Arithmetic works much like int
print(1.5 + 2.25)
print(5.0 / 2)
print(2.0 ** 3)

# 3. Floating-point precision
print(0.1 + 0.2)  # often displays 0.30000000000000004
# Many decimal fractions cannot be represented exactly in binary.
# For comparisons, use math.isclose() when appropriate.
import math
print(math.isclose(0.1 + 0.2, 0.3))

# 4. Conversion
print(float("3.14"))
print(float(7))  # 7.0

# 5. Formatting for display
amount = 19.9876
print(round(amount, 2))
print(f"${amount:.2f}")  # display with two decimal places

# 6. Special values
print(float("inf"))
print(float("-inf"))
print(float("nan"))  # not-a-number; NaN is not equal to itself

# For exact decimal currency calculations, consider decimal.Decimal.
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))

# EXERCISES
# 1. Calculate the average of 8.5, 9.0, and 7.5.
# 2. Convert "15.75" to float and multiply by 2.
# 3. Check whether 0.1 + 0.2 is close to 0.3.
# 4. Format 1234.5 to show two decimal places.

"""
COMPLEX (complex) — numbers with real and imaginary parts
Run: python complex.py
A complex number has the form a + bj, where j is sqrt(-1).
Python uses j (not i) for the imaginary unit.
"""

# 1. Creating complex values
z = 3 + 4j
another = complex(2, -5)  # 2 - 5j
print(z, type(z))

# 2. Access the parts
print(z.real)  # 3.0
print(z.imag)  # 4.0

# 3. Arithmetic
a = 1 + 2j
b = 3 - 1j
print(a + b)
print(a * b)
print(a / b)
print(a ** 2)

# 4. Conjugate and magnitude
print(z.conjugate())  # 3 - 4j
print(abs(z))         # magnitude: 5.0

# 5. Complex numbers are useful in signal processing, physics, and mathematics.
# The cmath module provides complex-aware mathematical functions.
import cmath
print(cmath.phase(z))  # angle in radians
print(cmath.sqrt(-1))  # 1j

# Complex values cannot be ordered with < or >.
# Equality is supported: (2 + 0j) == 2 is True.

# EXERCISES
# 1. Create -2 + 6j and print its real and imaginary parts.
# 2. Add (2+3j) and (4-5j).
# 3. Find the magnitude of 5+12j.
# 4. Compute the conjugate of 7-2j.

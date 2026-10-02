"""
TUPLE (tuple) — ordered, immutable collections
Run: python tuple.py
Tuples resemble lists, but their element references cannot be reassigned.
"""

# 1. Creating tuples
point = (4, 7)
colors = ("red", "green", "blue")
empty = ()
single = (5,)  # comma is essential for a one-item tuple
print(point, type(point), type((5)))

# Parentheses can often be omitted:
coordinates = 2, 8

# 2. Indexing and slicing
print(colors[0], colors[-1], colors[:2])

# 3. Tuples are immutable
# point[0] = 10  # TypeError
# A tuple may contain a mutable object, though that object can still change.
container = ([1, 2], "fixed")
container[0].append(3)
print(container)

# 4. Packing and unpacking
x, y = point
print(x, y)
first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)

# 5. Methods and membership
sample = (1, 2, 2, 3)
print(sample.count(2), sample.index(3), 1 in sample)

# 6. Returning multiple values from a function
def min_and_max(values):
    return min(values), max(values)

low, high = min_and_max([8, 2, 10, 4])
print(low, high)

# EXERCISES
# 1. Create a tuple with three cities.
# 2. Unpack a tuple (2026, 10, 2) into year, month, day.
# 3. Count how many times "a" occurs in ("a", "b", "a").
# 4. Write a function that returns both the sum and length of a list.

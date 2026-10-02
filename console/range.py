"""
RANGE (range) — immutable arithmetic sequences of integers
Run: python range.py
range is memory-efficient: it represents a sequence without storing every number.
"""

# 1. range(stop): starts at 0 and stops before stop
print(list(range(5)))  # [0, 1, 2, 3, 4]

# 2. range(start, stop)
print(list(range(2, 7)))  # 2, 3, 4, 5, 6

# 3. range(start, stop, step)
print(list(range(1, 10, 2)))  # odd numbers below 10
print(list(range(5, 0, -1)))  # countdown

# 4. Commonly used with for loops
for number in range(3):
    print("Iteration", number)

# 5. Membership, length, indexing, slicing
sequence = range(10, 20, 2)
print(14 in sequence, len(sequence), sequence[2], sequence[1:4])

# 6. range is not a list, but can be converted when needed
numbers = list(range(4))
print(numbers, type(numbers))

# The step cannot be zero. The stop value is always excluded.

# EXERCISES
# 1. Print integers from 1 through 10 using range().
# 2. Print even numbers from 2 through 20.
# 3. Create a countdown from 5 to 1.
# 4. How many values are in range(3, 30, 4)?

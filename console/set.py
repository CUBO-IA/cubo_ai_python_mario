"""
SET (set) — unordered collections of unique, hashable elements
Run: python set.py
Sets remove duplicates and are useful for membership and set operations.
"""

# 1. Creating sets
numbers = {1, 2, 2, 3}
empty = set()  # {} creates an empty dictionary, not a set
print(numbers, type(numbers))

# 2. Add, remove, and test membership
numbers.add(4)
numbers.discard(10)  # safe if absent
numbers.remove(2)    # raises KeyError if absent
print(3 in numbers, numbers)

# 3. Set operations
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # union
print(A & B)  # intersection
print(A - B)  # difference: in A, not B
print(A ^ B)  # symmetric difference: in exactly one set

# Equivalent methods: A.union(B), A.intersection(B), etc.
print(A.issubset({1, 2, 3, 4}))
print(A.isdisjoint({8, 9}))

# 4. Remove duplicates from a sequence (original order is not guaranteed)
unique = set(["apple", "pear", "apple"])
print(unique)

# 5. Elements must be hashable; lists and dictionaries cannot be set members.
# invalid = {[1, 2], [3, 4]}  # TypeError

# EXERCISES
# 1. Make a set from [1, 1, 2, 3, 3, 3].
# 2. Find shared interests between two sets.
# 3. Find values present in A but not B.
# 4. Check whether {2, 4} is a subset of {1, 2, 3, 4, 5}.

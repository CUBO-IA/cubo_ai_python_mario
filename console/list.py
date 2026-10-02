"""
LIST (list) — ordered, mutable collections
Run: python list.py
Lists can contain mixed types, duplicates, and nested lists.
"""

# 1. Creating lists
numbers = [10, 20, 30]
mixed = ["Ada", 36, True]
empty = []
print(numbers, type(numbers))

# 2. Indexing and slicing (like strings)
print(numbers[0], numbers[-1], numbers[1:])
numbers[1] = 99  # lists are mutable
print(numbers)

# 3. Add and remove elements
numbers.append(40)          # add one item
numbers.extend([50, 60])    # add multiple items
numbers.insert(1, 15)       # insert at index
numbers.remove(99)          # remove first matching value
last = numbers.pop()        # remove and return last item
del numbers[0]              # delete by index
print(numbers, "popped:", last)

# 4. Search and count
values = [2, 4, 2, 6]
print(2 in values, values.index(4), values.count(2))

# 5. Useful built-ins and methods
print(len(values), sum(values), min(values), max(values))
values.sort()               # sorts in place
values.reverse()            # reverses in place
print(values)
sorted_values = sorted([3, 1, 2])  # creates a new sorted list

# 6. Looping
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

# 7. Nested lists
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # row 2, column 1 -> 3

# 8. Copying: assignment creates an alias, not a separate list.
original = [1, 2]
alias = original
copy = original.copy()
alias.append(3)
print(original)  # [1, 2, 3]
print(copy)      # [1, 2]

# EXERCISES
# 1. Create a list of five favorite subjects.
# 2. Append a new subject, then remove one.
# 3. Find the largest and smallest numbers in a list.
# 4. Make a copy of a list and show that changing it leaves the original alone.
# 5. Build a 2x2 matrix and print its bottom-right value.

"""
FROZENSET (frozenset) — immutable sets
Run: python frozenset.py
A frozenset supports set operations but cannot be changed after creation.
"""

# 1. Create a frozenset
permissions = frozenset(["read", "write", "read"])
print(permissions, type(permissions))

# 2. Set operations work
other = frozenset(["read", "execute"])
print(permissions | other)
print(permissions & other)
print(permissions - other)
print("read" in permissions)

# 3. Unlike set, no add/remove methods are available.
# permissions.add("admin")  # AttributeError

# 4. Since it is immutable and hashable (if its elements are hashable),
# a frozenset can be a dictionary key or a member of another set.
access = {permissions: "standard"}
print(access[permissions])
collection = {frozenset([1, 2]), frozenset([3, 4])}
print(collection)

# EXERCISES
# 1. Create a frozenset of three file permissions.
# 2. Find the intersection of two frozensets.
# 3. Try to add an item and observe the exception (uncomment the line).
# 4. Use a frozenset as a dictionary key.

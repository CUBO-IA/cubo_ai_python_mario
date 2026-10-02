"""
BYTES (bytes) — immutable sequences of byte values
Run: python bytes.py
Each byte is an integer from 0 through 255. Bytes are used for binary data.
"""

# 1. Create bytes
raw = b"Hello"
from_numbers = bytes([65, 66, 67])
print(raw, from_numbers, type(raw))

# 2. Indexing returns an integer; slicing returns bytes
print(raw[0], raw[:2])

# 3. Text and bytes are different types
text = "café"
encoded = text.encode("utf-8")
print(encoded)
decoded = encoded.decode("utf-8")
print(decoded)

# 4. Bytes are immutable
# raw[0] = 72  # TypeError

# 5. Useful operations
print(b"ell" in raw)
print(b"A" + b"B")
print(bytes([0, 10, 255]))

# 6. Read binary files with mode "rb"; write with "wb".
# with open("sample.bin", "wb") as file:
#     file.write(encoded)
# with open("sample.bin", "rb") as file:
#     content = file.read()

# EXERCISES
# 1. Create bytes from [80, 121, 116, 104, 111, 110].
# 2. Encode "Python" to UTF-8 and decode it back.
# 3. What does indexing b"ABC"[1] return?
# 4. Explain the difference between a string and bytes.

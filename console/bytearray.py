"""
BYTEARRAY (bytearray) — mutable sequences of byte values
Run: python bytearray.py
Like bytes, each element is 0–255; unlike bytes, bytearray can be modified.
"""

# 1. Create a bytearray
data = bytearray(b"Hello")
print(data, type(data))

# 2. Modify individual bytes
data[0] = ord("Y")
print(data)  # bytearray(b'Yello')

# 3. Append and extend integer byte values
data.append(ord("!"))
data.extend([10, 65])
print(data)

# 4. Convert between bytes and bytearray
immutable = bytes(data)
mutable_again = bytearray(immutable)
print(immutable, mutable_again)

# 5. Decode byte data into text when it represents encoded text
message = bytearray("Hola".encode("utf-8"))
print(message.decode("utf-8"))

# Bytearray is useful when binary data must be edited in place.
# Values outside 0..255 raise ValueError.

# EXERCISES
# 1. Create bytearray(b"cat") and change c to b.
# 2. Append the byte value for "!" using ord().
# 3. Convert a bytearray to bytes.
# 4. Decode a bytearray containing UTF-8 encoded "hello".

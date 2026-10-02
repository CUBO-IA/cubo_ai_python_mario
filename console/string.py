"""
STRING (str) — text
Run: python string.py
Strings are immutable sequences of Unicode characters.
"""

# 1. Creating strings
name = "Ada"
message = 'Hello, Python!'
multiline = """This text
uses multiple lines."""
print(name, type(name))

# 2. Indexing starts at zero; negative indices count from the end.
word = "Python"
print(word[0], word[1], word[-1])

# 3. Slicing: [start:stop:step], stop is excluded
print(word[0:3])   # Pyt
print(word[2:])    # thon
print(word[::-1])  # nohtyP

# 4. Strings are immutable: create a new string rather than changing a character.
# word[0] = "J"  # TypeError
word = "J" + word[1:]
print(word)

# 5. Common methods (methods return new strings)
text = "  learn Python well  "
print(text.strip())
print(text.lower())
print(text.upper())
print(text.replace("well", "daily"))
print("a,b,c".split(","))
print("-".join(["2026", "10", "02"]))
print("Python".startswith("Py"), "Python".endswith("on"))

# 6. Length, membership, and iteration
print(len("hello"))
print("Py" in "Python")
for character in "AI":
    print(character)

# 7. Formatting: f-strings are readable and useful
person = "Maya"
age = 20
print(f"{person} is {age} years old.")
print(f"Next year: {age + 1}")

# 8. Convert to string
print(str(2026), type(str(2026)))

# EXERCISES
# 1. Store your first name and print its length.
# 2. Print the first and last characters of "programming".
# 3. Turn "  HELLO world  " into "hello world".
# 4. Use an f-string to introduce a person and their age.
# 5. Split "red|green|blue" into a list.

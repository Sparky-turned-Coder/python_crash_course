import this

# Below is the philosophy behind the Python programming language
print(this)
print()
print()
print()


# =======================
# Multiple Assignment
# =======================

# You can assign values to more than one variable using just a single line of code
#       For example, here's how you can initialize the variables x, y, and z:

x, y, z = 1, 2, 3
ashley_age, kyle_age, chris_age = 33, 35, 37
filename1, filename2, filename3 = "rust.txt", "python.txt", "typescript.txt"

print(x, y, z)

print(
    f"The ages of me and my siblings, youngest to oldest, is: {ashley_age, kyle_age, chris_age}"
)  # I just noticed, this returns a list in parenthesis...

print(f"Filenames in this folder are: {filename1, filename2, filename3}")

# ===========
# Constants
# ===========

# A constant is a variable whose value stays the same thoughout the life of a program.
# Python DOES NOT have built-in constant types, but Python programmers use all capital
#   letters to indicate a variable should be treated as a constant and never be changed.

MAX_CONNECTIONS = 5000
GOKU = "Over 9,000!"

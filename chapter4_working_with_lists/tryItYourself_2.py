# =========================
# 4-3. Counting to Twenty
# =========================

# Use a for-loop to print the numbers from 1 to 20, inclusive.

numbers = []
for number in range(1, 21):
    numbers.append(number)
print(numbers)
print("_______________________________")

# ==================
# 4-4. One Million
# ==================

# Make a list of the numbers from one to one million, and then use a for-loop to print the numbers.
# [If the output is taking too long, stop it by pressing C-c or by closing the terminal window]

mil_numbers = list(range(1, 11))
# Changed one million to eleven so I'm not printing this every time I run terminal.
for number in mil_numbers:
    print(number)
print()
print("_______________________________")

# ========================
# 4-5. Summing a Million
# ========================

# Make a list of the numbers from one to one million, and then use the min() and max() functions to make
# sure your list actually starts at one and ends at one million. Also, use the sum() function to see how
# quickly Python can add a million numbers.

mil_numbers2 = list(range(1, 1_000_001))
print(min(mil_numbers2))
print(max(mil_numbers2))
print(sum(mil_numbers2))
print()
print("_______________________________")

# ==================
# 4-6. Odd Numbers
# ==================

# Use the third arguement of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for-loop to print each number.

odd_numbers = list(range(1, 20, 2))
for number in odd_numbers:
    print(number)
print()
print("_______________________________")
# ============
# 4-8. Cubes
# ============

# A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python.
# Make a list of the first 10 cubes, (that is, the cube of each integer from 1 through 10), and use a for-loop to
# print out the value of each cube.

cubed_list = list(range(1, 11))
for number in cubed_list:
    print(f"{number} cubed is: ", number**3)
print()
print("_______________________________")


# =========================
# 4-9. Cube Comprehension
# =========================

# Use a list comprehension to generate a list of the first 10 cubes.

cubed_list2 = [value**3 for value in range(1, 11)]
print(cubed_list2)
print()

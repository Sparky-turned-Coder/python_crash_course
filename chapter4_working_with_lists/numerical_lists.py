# NOTE: =====================
# Making Numerical Lists
# ==========================

# There are many reason to have to store sets of numbers. In data visualization, you'll almost always work with sets of numbers,
# such as temperatures, distances, population sizes, or latitude and longitude values, among other types of numerical sets.

# =============================
# Using the range() function
# =============================

# Python's range() function makes it easy to generate a series of numbers. For example, you can use the range() function
# to print a series of numbers like this:

for value in range(1, 5):
    print(value)
print()

# NOTE: range() prints only the numbers 1 through 4. This is another result of the off-by-one behavior you'll see often in programming languages.
#      You can also pass a single arguement in range(), and it will print those values beginning with zero:

for value in range(6):  # therefore, a range of '6' will print 0 - 5
    print(value)
print()

# =========================================
# Using range() to Make a list of Numbers
# =========================================

# If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function. When you wrap
# list() around a call to the range() function, the 'output'  will be a list of numbers.
# Using the previous example, convert that range() into a list():

numbers = list(range(1, 6))
print(numbers)
print()

# NOTE: You can also use the range() function to tell Python to skip numbers in a given range. If you pass a third arguement to range(), Python uses
#      that 'third' value as a step size when generating numbers:

even_numbers = list(range(2, 11, 2))
# range is 2 - 11.  The third arguement, '2', tells python to print every 2nd number.
# Therefore, range starts at 2 and then counts up by 2 until it reaches 11 and stops.
print(even_numbers)
print()

# NOTE: You can create almost any set of numbers you want to using the range() function. For example, consider how you might make a list of the first 10
# square numbers (that is, the square of each integer from 1 through 10). In Python, two asterisks (**) represent exponents.

# squares = []
# for value in range(1, 11):
#     square = value**2
#     squares.append(square)

# 2 lines below are a more concise way to write the 3 lines above. Instead of creating a new variable, we are immediately appending the result to our list.
# for value in range(1, 11):
#     squares.append(value**2)
#
# print(squares)
print()

# NOTE: Practice problem!!! Try to figure out how to implement

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print()
print(max(digits))
print()
print(sum(digits))
print()


# ======================
# List Comprehensions
# ======================

# Another way to generate the 'squares' list from above is list comprehension. A list comprehension allows you to generate this same list in just one line of code.
# A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.
# See below:

squares = [value**2 for value in range(1, 11)]
print(squares)
print()

# NOTE:   To use this syntax, begin with a descriptive name for the list, such as 'squares'. Next, open a set of square brackets and define the expression for
#        the values you want to store in the new list. In this example the expression is to generate the numbers you want to feed into the expression, and close
#        the square brackets. The for-loop in this example is 'for value in range(1, 11)', which feeds the values 1 through 10 into the expression value**2.
#        Note that no colon is used at the end of the for-statement.
#        The result is:
#        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

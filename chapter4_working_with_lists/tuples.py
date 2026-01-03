# ============================
# Tuples - an immutable list
# ============================

# Lists work well for storing collections of items that can change throughout the life of a program. The ability to
# modify lists is particularly important when you're owrking with a list of users on a website or a list of characters
# in a game. However, sometimes you'll want to create a list of items that cannot change. Tuples allow you to do just
# that. Python refers to values that cannot change as 'immutable', and an immutable list is called a tuple.

# NOTE: Immutable - Python refers to values that cannot change as immutable. An immutable list is called a tuple.


# ==================
# Defining a tuple
# ==================

# A tuple looks just like a list, except you use parenthesis instead of square brackets. Once you define a tuple,
# you can access individual elements by using each item's index, just as you would for a list.

# For example, let's say we have a rectangle that should always be a certain size. We can ensure
# that its size doesn't change by putting the dimensions into a tuple:

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print()

# What happens if we try to change one of the items in the tuple 'dimensions'?
# dimensions[0] = 250

# ERROR: 'tuple' object does not support item assignment

# NOTE: Tuples are technically defined by the presence of a comma; the paranthesis make them look neater and more readable.
#      If you you want to define atuple with one element, you need to include a trailing comma:

my_t = (3,)
# output of 'print(my_t[0])' is: 3
# It doesn't often make sense to build a tuple with one element, but this can happen when tuples are generated automatically.

# =======================================
# Looping through all values in a Tuple
# =======================================

# You can loop over all the values in a tuple using a for-loop, just as you did with a list:

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
print()

# =====================
# Writing over a Tuple
# =====================

# Although you can't modify a tuple, you can assign a new value to a variable that represnts a tuple:

dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)
print()

# To reassign the values in a Tuple, assign the new values to the same variable that was used to store the original values.

# NOTE: When compared with lists, tuples are simple data structures. Use them when you want to store a set of values that
#      should not be changed throughout the life of a program.

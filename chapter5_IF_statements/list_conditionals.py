# CHECKING WHETHER A VALUE IS IN A LIST

# Sometimes it's important to check whether a list contains a certain value before taking
# action. For example, you might want to check whether a new username already exists in a
# list of current usernames before completing someone's registration on a website.

# In a list, we use the keyword 'in'.

requested_toppings = ["mushrooms", "onions", "pineapple"]
if "mushrooms" in requested_toppings:
    print("Yes, there are mushrooms in it.")

if "pepperoni" in requested_toppings:
    print("Yes, there are pepperonis.")
else:
    print("Nope, no pepperonis.")

# The keyword 'in' tells Python to check for the existence of 'mushrooms' and 'pepperoni'
# in the list 'requested_toppings'.

# CHECKING WHETHER A VALUE IS NOT IN A LIST

# Other times, it's important to know if a value does not appear in a list. You can use
# the keyword 'not in' in this situation.

banned_users = ["andrew", "caroline", "chris"]

user = input("What is your name? ")

if user.lower() not in banned_users:
    print("You are not banned. Have fun!")
else:
    print("You are banned for life!")


# BOOLEAN EXPRESSIONS

# As you learn more about programming, you'll hear the term BOOLEAN EXPRESSION at some point.
# A Boolean expression is just another name for a conditional test. A 'boolean value' is either
# TRUE or FALSE, just like the value of a conditional expression after is has been evaluated.

# Boolean values are often used to keep track of certain conditions, such as whether a game
# is running or whether a user can edit certain content on a website:

game_active = True
can_edit = False

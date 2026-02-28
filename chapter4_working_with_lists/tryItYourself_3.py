# ==============
# 4-10. Slices
# ==============

characters = [
    "gustave",
    "lune",
    "sciel",
    "maelle",
    "monoco",
    "verso",
    "esquie",
    "renoir",
    "clea",
]

# Using one of the programs you wrote in this chapter, add several lines to the end of the program
# that do the following:
print("List: ", characters)
print()
# Print the message 'The first three items in the list are:'  Then use a slice to print the first three items from that program's list.
print("The first three characters in this list are: ", characters[:3])
print()
# Print the message 'Three items from the middle of the list are:'  Then use a slice to print three items from the middle of the list.
print("Three characters from the middle of this list are: ", characters[3:6])
print()
# Print the message 'The last three items in the list are:'  Then use a slice to print the last three items from the list.
print("The last three characters in this list are: ", characters[6:9])
print()


# ===============================
# 4-11. My Pizzas, Your Pizzas
# ===============================

pizzas = ["pepperoni", "extra cheese", "sausage"]
friend_pizzas = pizzas[:]
print("Original pizza list: ", pizzas, "\n")

# Start with your program from exercise 4-1. Make a copy of the list of pizzas, and call it 'friend_pizzas'.
# Then, do the following:

# Add a new pizza to the original list.
pizzas.append("bacon")

# Add a different pizza to the list 'friend_pizzas'.
friend_pizzas.append("pineapple")

# Prove that you have two seperate lists. Print the message 'My favorite pizzas are:', and then use a for-loop to print the first list.
# Print the message 'My friend's favorite pizzas are:', and then use a for-loop to print the second list. Make sure each new
# pizza is stored in the appropriate list.
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print()
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
print()


# ==================
# 4-12. More Loops
# ==================

# All versions of 'foods.py' in this section have avoided using for-loops when printing, to save space. Choose a version of foods.py and
# write two for-loops to print each list of foods.

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are: ")
for food in my_foods:
    print(food)
print()
nprint("My friend's favorite foods are: ")
for food in friend_foods:
    print(food)
print()

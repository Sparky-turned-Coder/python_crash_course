# =====================
#  Introducing Lists
# =====================

# What is a list?
#   A list is a collection of items in a particular order.

# In python, square brackets [] indicate a list. Individual elements in a list are
#  seperated by a commas.

# Example:
football_teams = ["Titans", "Patriots", "Ravens", "Bucaneers", "Lions"]

# If you ask Python to print a list, it returns its representation of the list, including the [].
print(football_teams)


# ==============================
# Assessing elements in a list
# ==============================

# You can access any element in a list by telling Python the position, or INDEX, of the item desired.
# You can use f-strings to create a message based on a value from a list:

football_teams = ["titans", "patriots", "ravens", "bucaneers", "lions"]
message = f"My hometown team is: {football_teams[0].title()}."

print(message)


# NOTE: you can use 'string methods' on any element in your list

football_teams = ["titans", "patriots", "ravens", "bucaneers", "lions"]
print(football_teams[1].title())

# NOTE: index positions start at 0.   (element[0], [1], element[2], element[3]...)

football_teams = ["titans", "patriots", "ravens", "bucaneers", "lions"]
print(football_teams[0])
print(football_teams[3])
print()
print()
print()


# =========================================
# Modifying, Adding, and Removing Elements
# =========================================

# NOTE: Most lists you create will be DYNAMIC,
#      meaning you'll build a list and then add and remove elements from it as your program runs its course.

#      FOR EXAMPLE, you might create a game in which a player has to shoot aliens out of the sky. You could
#      store the initial set of aliens in a list and then remove an alien from the list each time it is shot down.
#      Each time a new alien appears on the screen, you add it to the list. Your list of aliens will increase
#      and decrease in length throughout the course of the game.

# ============
# Modifying
# ===========

# Change the value saved for a specified element:

pokemon = ["squirtle", "garchomp", "breloom", "mudkip", "lugia", "bagon", "celebi"]
print(pokemon)

pokemon[4] = "abra"
pokemon[6] = "bulbasaur"
print(pokemon)

# Appending elements to the END of a list

# Simplest way to add to a list is to append the item to the list. When you append an item to a list, the new
# element is added to the end of the list.

pokemon.append("pidgey")
print("My favorite pokemon are: ", pokemon)

print()

# The append() method makes it easy to BUILD LISTS DYNAMICALLY.

# For example, you can start with an empty list and then fill the list with a series of append() calls:

legendary_pokemon = []

legendary_pokemon.append("celebi")
legendary_pokemon.append("lugia")
legendary_pokemon.append("kyogre")
legendary_pokemon.append("ho-oh")
legendary_pokemon.append("mew")

print("My favorite legendary pokemon are: ", legendary_pokemon)
print()
print()
# NOTE: Building lists this way is very common, as you often won't know the data your users want to store in
#      a program until after the program is running.

# To put your users in control, start by defining an empty list that will hold the user's values.
# Then you will simply append each new value provided to the list you just created.

fav_pokemon = []
# fav_pokemon.append(input("What is your favorite pokemon? "))
print(fav_pokemon)

# ================================
# Inserting elements from a list
# ================================

# Instead of just using append() to add a new element to the end of a list, you can also add a new element at
# any position in your list by using the insert() method.

print(pokemon)

pokemon.insert(0, "gligar")
print(pokemon)

# This operation shifts every other value in the list on position to the right.

# ================================
# Removing elements from a list
# ================================

# Often you'll want to remove an item or a set of items from a list, such as in our alien example above.
# Every time a player shoots down an alien, you can remove that alien from your list of active aliens.
# Or when a user decides to cancel their account on a web application you've created, you'll want to remove
# them from the list of active users.

# NOTE: Removing an Item using the 'del' statement

# If you know the position  of the item you want to remove from a list, you can use the del statement.

print(pokemon)

del pokemon[
    0
]  # remove gligar from the list of pokemon because we know its position in the list is zero
print(pokemon)

del pokemon[
    7
]  # remove pidgey from the list because we know its position in the list is seven
print(pokemon)
print()
print()

# NOTE: Removing an Item using the pop() method

# Sometimes you'll want to use the value of an item after you remove it from a list.
#   For example, you might want to get the x and y position of an alien that was just shot down, so you
#   can draw an explosion at that position. In a web application, you might want to remove a user from
#   a list of active memebers and then add that user to a list of inactive members.

# The pop() method removes the last item in a list, but it lets you work with that item after removing it.
# The term POP comes from thinking of a list as a stack of items and POPPING one item off the top of the stack.
# The top of the stack == the end of a list.

print(pokemon)

popped_pokemon = pokemon.pop()
print("List of pokemon after popping one from the list is: ", pokemon)
print("Pokemon we popped from the list was: ", popped_pokemon)

# In conclusion, what we did was we printed the original list of pokemon. Then we popped a pokemon from the
# end of the list. Then we printed the new list of pokemon. Then we printed the pokemon we popped seperately.

# NOTE: How might this pop() method be useful?
#   Imagine that the list of pokemon are stored are in chronilogical order, according to when we caught them in the wild.
#   If this is the case, we can use pop() to print a statement about the most recent pokemon we caught:

print(pokemon)

last_pokemon_caught = pokemon.pop()
print(
    f"The most recent pokemon we caught and added to our pokedex was a {last_pokemon_caught.title()}."
)

# NOTE: Popping items from ANY position in a list
#  You can use pop() to remove an item from any position in a list if you know what that position is.
#  The index of the item you want to pop() will be inside pop's parenthesis. (method's arguement)

# list up to this point is: ['squirtle', 'garchomp', 'breloom', 'mudkip', 'abra']

print(pokemon)

first_pokemon = pokemon.pop(0)
print(
    f"The first pokemon I ever earned was a {first_pokemon.title()}. Given to me by Professor Oak."
)

pokemon.insert(
    0, first_pokemon
)  # here I returned the pokemon I popped back into the list in the same position I removed it from.
print()
print()

# NOTE: REMEMBER! Each time you use pop(), that item you're working with is no longer stored in a list.
#  If you're unsure whether to use the 'del' statement or the pop() method, here's a simple way to decide:
#  when you want to delete an item from a list and never use that item again in any way, use the 'del' statement.
#  if you think you will want to use the item when you remove it, use the pop() method.
#       This might sound obvious, but if you think about it while you're coding it will make total sense.

# ===========================
# Removing an item by value
# ===========================

# Sometimes you WILL NOT know the position of an item you want to remove from a list. If you only know the value that was stored in
# the item you want to remove, you can use the remove() method.
pokemon = ["squirtle", "garchomp", "breloom", "mudkip", "abra"]
print(pokemon)

pokemon.remove("garchomp")
# Pretending that our list of pokemon was hundreds of pocket monsters long, we don't know what position Garchomp is in our list.
# Therefore, we use the remove() method by inserting the string 'garchomp' inside the method's arguement. (The parenthesis)
# This allows us to remove an item from our list even if we don't know the index position.

print(pokemon)
print()
print()


# NOTE: We can still use the item we removed from our list with the remove() method by storing it in a new variable. But we store
#  the string value in a variable BEFORE removing it from the list. Thus, we use: remove(variable)

pokemon = ["squirtle", "garchomp", "breloom", "mudkip", "abra"]
print(pokemon)

too_strong = "garchomp"
pokemon.remove(too_strong)
print(pokemon)
print(f"\n{too_strong.title()} is way too strong to be using in the early game.")

# NOTE: The remove() method deleted only the first occurence of the value you specify. If there's a possibility the value appears
#      more than once in the list, you'll need to use a loop to make sure all occurrences of the value are removed.

# ===============================
# TRY IT YOURSELF (EXERCISES)
# ===============================


print()

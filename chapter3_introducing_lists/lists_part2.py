# =====================
# Organizing a List
# =====================

# Often, your lists will be created in an unpredicatable order, because you can't always control the order in which your users provide their data.
# Although this is unavoidable in most circumstances, you'll frequently want to present your information in a particular order. Sometimes you'll
# want to preserve the orignal order of your list, and other times you'll want to change the original order. Python provides a number of different
# ways to organize your lists, depending on the situation.

# ====================================================
# Sorting a List Permanently with the sort() Method
# ====================================================

# Python's sort() method makes it relatively easy to sort a list. Imagine we have a list of pokemon and want to change the order of the list to sort
# them alphabetically. To keep the task simple, let's assume that all the values in the list are lowercase.

pokemon = ["pikachu", "charmander", "squirtle", "mudkip", "torchic", "sudowoodo"]
pokemon.sort()
print(pokemon)
print()

# NOTE: The sort() method changes the order of the list permanently.

# You can also sort this list in reverse-alphabetical order by passing the argument 'reverse=True' to the sort() method.

pokemon = ["pikachu", "charmander", "squirtle", "mudkip", "torchic", "sudowoodo"]
pokemon.sort(
    reverse=True
)  # we pass the 'reverse=True' arguement through our sort method to reverse the list alphabetically
print(pokemon)
print()


# =======================================================
# Sorting a List Temporarily with the sorted() Function
# =======================================================

# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. The sorted() function lets you display
# your list in a particular order, but doesn't affect the actual order of the list. It only displays the list a specified way temporarily.

pokemon = ["pikachu", "charmander", "squirtle", "mudkip", "torchic", "sudowoodo"]

print(f"Here is the original list: {pokemon}\n")

print(f"Here is the sorted list: {sorted(pokemon)}\n")

print(f"Here is the original again: {pokemon}\n")

# NOTE: Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. There are several ways to interpret capital
#      letters when determining a sort order, and specifying the exact order can be more complex than we want to deal with at this time. However,
#      most approaches to sorting will build directly  on what you learned in this section.

# ===================================
# Printing a List in Reverse Order
# ===================================

# To reverse the original order of a list, you can use the reverse() method.

pokemon = ["pikachu", "charmander", "squirtle", "mudkip", "torchic", "sudowoodo"]
pokemon.sort()  # We sort the list above alphabetically
print(pokemon)
print()

pokemon.reverse()  # We reverse the alphabetically sorted list from above
print(pokemon)
print()

# NOTE: Keep in mind that the reverse() method doesn't necessarily reverse the order of the list alphabetically, it just reverses whatever order the list currently is in.

# NOTE: The reverse() method sorts the list permanently, just like the sort() method. So, if you ever use the sort() method to sort a list, you can then use the reverse()
#      method to reverse it back to the original.

# =================================
# Finding the Length of a List
# =================================

# You can quickly find the length of a list by using the len() function.

pokemon = ["pikachu", "charmander", "squirtle", "mudkip", "torchic", "sudowoodo"]
poke_list_length = len(pokemon)
print(f"The length of our list of pokemon is: {poke_list_length}.\n")

# NOTE: Notice that the number len() returns is an actual count of all the items in the list. Which is why it doesn't start with zero.

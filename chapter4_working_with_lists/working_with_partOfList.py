# =============================
# Working with Part of a List
# =============================

# In chapter 3 you learned how to access single elementsk in a list, and in this chapter you've been learning
# how to work through all the lemeents in a list. You can also work with a specific group of items in a list,
# called a 'slice' in Python.

# ================
# Slicing a List
# ================

# To make a slice, you specify the index of the first and last elements you want to work with. As with the range()
# function, Python stops one item before the second index you specify. To output the first three elements in a list,
# you would request indices 0 through 3, which would return elements 0, 1, and 2.

characters = [
    "gustave",
    "lune",
    "sciel",
    "maelle",
    "monoco",
    "verso",
    "esquie",
    "renoir",
]
print("Print a slice from characters with [0:3] ", characters[0:3])
# We sliced the first three entries from our list in a print statement
print()

print("Print a slice from characters with [1:4] ", characters[1:4])
print()

print("Print a slice from characters with [4:8] ", characters[4:8])
# Notice, our list doesn't extend to 8 indices, but when called to it still tries to count that high, which is why we can print index 7.
print()

# If you omit the first index in a slice, Python automatically starts your slice at the beginning.
print("Print a slice from characters with [:4] ", characters[:4])
# So we printed out characters ranging from beginning of list through '4'. So we printed 0, 1, 2, and 3
print()

# A similar slice to the above example works if you want a slice that includes to the end of the list. Just omit the second index instead of the first:
print("Print a slice from characters with [3:] ", characters[3:])
# So we printed out characters ranging from index '3' through the end of the list. So we printed 3, 4, 5, 6, and 7
print()

# Remember, negative numbers count back from the end of a list. So, if we want to print out the last 4 elements in the list:
print(characters[-4:])
print()

# This will continue to work as the list of characters grows, always printing the last 4 elements in the list, even if they change.
characters.append("alicia")
characters.append("clea")
characters.append("nevron")
print(characters[-4:])
print()

# updated_list = ['gustave', 'lune', 'sciel', 'maelle', 'monoco', 'verso', 'esquie', 'renoir', 'alicia', 'clea', 'nevron']

# ==========================
# Looping through a Slice
# ==========================

# You can use a slice in a for-loop if you want to loop through a subset of the elements in a list. Let's loop through the first three
# characters and print names as part of a team roster:

print("Here are the first three characters in my battle lineup:")
# Remember, if the first index is omitted in a slice, Python automatically begins the slice at zero. Thus, we get the indices 0, 1, and 2.
for char in characters[:3]:
    print(" - ", char.title())
print()

# Another use example of slices. If you create a game that records high scores, you can arrange your list in descending order and then slice
# the first three scores since they're the highest:

top_scores = [93, 35, 64, 12, 78, 89, 63, 85]
top_scores.sort(reverse=True)
# sort() arranges a list of integers in ascending order.
# Therefore, we set reverse=True so we reverse that arrangement to descending order.
print("Your 3 highest recorded scores are: ", top_scores[:3])
print()

# ================
# Copying a List
# ================

# Often, you'll want to start with an existing list and make an entirely new list based on the first one.
# To copy a list, make a slice that omits both the first and second indexes ([:]). This tells Python to make a
# slice that starts at the first item and ends with the last item, producing a copy of the entire list.

my_foods = ["pizza", "falafel", "cake"]
friend_foods = my_foods[:]
# by slicing the entire list, which we then assign to a new variable, we have essentially created a copy of it.

print("My favorite foods are: ", my_foods)
print()
print("My friend's favorite foods are: ", friend_foods)
print()

# Another example: We assign a list of values to 'pokemon'. Then we assign the slice of pokemon ([:]) to a new variable called 'pokemon_copy'
my_pokemon = ["pikachu", "squirtle", "charmander"]
his_pokemon = my_pokemon[:]
# my_pokemon = his_pokemon  >>> This does not work. See NOTE below.

# And to show that the 'copy' analogy holds, here we append each one and can see the proof:
my_pokemon.append("mudkip")
his_pokemon.append("torchic")
print("My pokemon: ", my_pokemon)
print("Friend's pokemon: ", his_pokemon)
print()

# NOTE: We cannot simply set my_pokemon equal to his_pokemon. If we do this, we are telling Python to
#      associate a second variable with the same list. So now we just have a list with 2 names, essentially.
#      Therefore, if we make a change to one of them, it will change the other one accordingly.
#      This means we cannot edit each one individually. One always equals the other.

# # ==============================
# #       Try it yourself
# # ==============================
#
# # NOTE: 3-8. Seeing the World - think of at least 5 places in the world you'd like to visit.
#
# # Steps:
#
# # store the locations in a list. List should NOT be in alphabetical order.
# locations = ["hong kong", "london", "sydney", "new york", "los angeles"]
#
# # print your list in its original order. Don't worry about printing the list neatly; just print it as a raw Python list.
# print(locations)
# print()
#
# # Use sorted() to print your list in alphabetical order without modifying the actual list.
# print(sorted(locations))
# print()
#
# # Show that your list is still in its original order by printing it.
# print(locations)
# print()
#
# # Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# print(sorted(locations, reverse=True))
# print()
#
# # Show that your list is still in its original order by printing it again.
# print(locations)
# print()
# # Use reverse() to change the order of your list. Print the list to show its order has been changed.
# locations.reverse()
# print(locations)
# print()
#
# # Use reverse() to change the order of your list again. Print the list to show its back to its original order.
# locations.reverse()
# print(locations)
# print()
#
# # Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.
# locations.sort()
# print(locations)
# print()
#
# # Use sort() to change your list so it's stored in reverse-alphabetical order. Print the list to show that its order has changed.
# locations.sort(reverse=True)
# print(locations)
# print()
#
# # Oh yeah. Let's DO THIS!!!!!
#
# # NOTE: 3-9. Dinner Guests
#
# # Working with one of the programs from Exercises 3-4 through 3-7, use len() to print a message indicating the number of people you're inviting to dinner.
#
# guest_list = ["J.R.R. Tolkien", "Linus Torvaldi", "Walt Disney"]
# print(f"I have decided to invite {len(guest_list)} lucky people to dinner tonight!\n")

# NOTE: 3-10. Every Function

# Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like.
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

# A list of Favorite Pokemon
pokemon = [
    "mudkip",
    "ho-oh",
    "kyogre",
    "garchomp",
    "roserade",
    "dragonite",
    "gligar",
    "flygon",
    "arbok",
    "mewtwo",
    "rayquaza",
    "sharpedo",
    "heracross",
    "stonchkrow",
]

# What we learned this chapter: sort() method, reverse() method, sorted() function, len() function, passing 'reverse=True' arguement in sort()

print(
    f"I have created a list of my favorite pokemon off the top of my head. There are {len(pokemon)} pokemon in this list.\n"
)

print("Here is our original list: \n")
print(pokemon)
print()
print("Here is that same list reversed: \n")
pokemon.reverse()
print(pokemon)
print()

print("Here is our original list:\n")
print(pokemon)
print()
print("Here is our list sorted alphabetically: \n")
pokemon.sort()
print(pokemon)
print()

print("Here is our list sorted alphabetically again: \n")
# we didn't call the sort() method for this because we already did above. Remember sort() is permanent.
print(pokemon)
print()
print("Here is the same list sorted reverse-alphabetically: \n")
pokemon.sort(reverse=True)
print(pokemon)
print()


print("Here is our list using the temporary 'sorted' function: ")
print(sorted(pokemon))
print()
print(
    "Here is our list of pokemon. It should, at this point, be in reverse-alphabetical order: \n"
)
print(pokemon)
print()
print()
print()

print("Let's use a few other things we learned with lists . . .")
print()
pokemon.reverse()
print(f"So here's the list again: {pokemon}\n")

print(
    "Pull the seventh pokemon in the list. To get the seventh pokemon, you'll use index 6."
)
print(pokemon[6])
print()

print(
    "Pull the last pokemon from the list. If you've lost track of how many there are, use index -1."
)
print(pokemon[-1])
print()

print("Display the first three pokemon in the list.")
print(pokemon[0], pokemon[1], pokemon[2])
print()

print("Add a new pokemon to the list.")
pokemon.append("ludicolo")
print(pokemon)
print()

print("Add another new pokemon, but add it at the beginning of the list.")
pokemon.insert(0, "nuzlocke")
print(pokemon)
print()

print(
    "Add another pokemon in the middle of the list. Use len() if you can't remember how many there currently are."
)
print(len(pokemon))
pokemon.insert(7, "pikachu")
print(pokemon)
print()


pokemon = [
    "mudkip",
    "ho-oh",
    "kyogre",
    "garchomp",
    "roserade",
    "dragonite",
    "gligar",
    "flygon",
    "arbok",
    "mewtwo",
    "rayquaza",
    "sharpedo",
    "heracross",
    "stonchkrow",
]


print(
    "Let's go above and beyond and see if we can remember how to turn this into a dictionary..."
)
print()

pokemon_dict = [
    {"name": "mudkip", "type": "water", "weaknesses": "electric/grass"},
    {"name": "torchic", "type": "fire", "weaknesses": "water/ground/rock"},
    {"name": "kyogre", "type": "water", "weaknesses": "electric/grass"},
    {"name": "gabite", "type": "dragon", "weaknesses": "dragon/ice/fairy"},
    {"name": "budew", "type": "grass", "weaknesses": "fire/bug/flying/ice"},
    {"name": "bagon", "type": "dragon", "weaknesses": "dragon/ice/fairy"},
    {"name": "ekans", "type": "poison", "weaknesses": "psychic/ground"},
    {"name": "mewtwo", "type": "psychic", "weaknesses": "dark/ghost/bug"},
    {"name": "caterpie", "type": "bug", "weaknesses": "fire/flying/rock"},
]

print("Our dictionary of pokemon: \n")
print(pokemon_dict)
print()

for pokemon in pokemon_dict:
    print(
        f"Name: {pokemon['name']}, Type: {pokemon['type']}, Weaknesses: {pokemon['weaknesses']}"
    )
print()

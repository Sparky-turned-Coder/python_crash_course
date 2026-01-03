# ===============================================
# Avoiding Index Errors When Working with Lists
# ===============================================

# There's one type of error that's common to see when you're working with lists for the first time.
# Let's say you have a list with three items, and you ask for the fourth item:

# pokemon = ["mudkip", "torchic", "treecko"]
# print(pokemon[3])
# IndexError: list index out of range

# As you can see, Python will still attempt to give you the item in index 3, but when it searches the list, no item in 'pokemon' has an index of 3.
# Because of the off-by-one nature of indexing in lists, this error is typical. People think the third item is item number 3, because they start
# counting at 1. But in Python(and other languages) the third item is number 2, because it starts indexing at 0.

# An index error means Python can't find an item at the index specified. If an index error occurs in your program, try adjusting the index you asking
# for by one. Then run the program again to see if the results are correct.

# NOTE: Keep in mind, when you want to access the last item in a list you should use the index -1. This will always work, even if your list has changed
#      size since the last time you accessed it.

pokemon = ["mudkip", "torchic", "treecko"]
print(f"The last item in this list of pokemon is: {pokemon[-1]}\n")

# The only time this approach will produce an error is if you call for index -1 on an empty list.

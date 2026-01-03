# =======================
# Looping through Lists
# =======================

# Often, you will want to run through all the entries in a list, performing the
# same task with each item. For example, in a game you might want to move every
# element on the screen by the same amount. In a list of numbers, you might want
# to perform the same statistical operation on every element. Or perhaps you'll
# want to display each headline from a list of articleson a website. When you want
# to do the same action with every item in a list, you can use Python's 'for' loop.

pokemon = ["articuno", "moltres", "zapdos"]
for mon in pokemon:
    print(mon)
print()

# We begin by defining a list, just as we did in the last chapter. Then we define
# a 'for-loop'. This line tells Python to pull a name from the list 'pokemon' and
# associate it with the variable 'mon'. Python then repeats these last two lines,
# once for each name in the list.

# NOTE: If it helps, read this code as: "For every every mon in this list of pokemon,
# print the mon's name."


# ===========================
# A Closer Look at Looping
# ===========================

# Looping is important because it's one of the most common ways a computer automates
# repetitive tasks.

# For example, in a simple loop like we used above, Python initially reads the first
# line of of the loop:
# NOTE:       for mon in pokemon:

# This line tells Python to retrieve the first value from the list 'pokemon' and
# associate it with the variable 'mon'.
# This first value is 'articuno'.

# Then, Python reads the next line:
# NOTE:       print(mon)

# Python prints the current value of 'mon', which is still 'articuno'.

# Then, Python returns to the first line of the loop and repeats the process:
# NOTE:       for mon in pokemon:

# Python retrieves the next name in the list, 'moltres', and associates that value
# with the variable 'mon'.

# Python then executes the line:
# NOTE:       print(mon)

# Python prints the current value of 'mon' again, which is now 'moltres'. Python
# repeats the entire loop once more with the last value in the list, 'zapdos'.
# Because no more values are in the list, Python moves on to the next line in the
# program. In this case nothing comes after the for loop, so the program ends.

# NOTE: Keep in mind, when writing your own for-loops, it's helpful to choose temporary
#       variable names that represent a meaningful connection to the list itself.
#       This helps when reading and understanding the code. For example, we used
#       'mon' for 'pokemon'. It's simple, but it also makes sense. Mon is a common
#       shorthand used in the general pokemon space. This also helps when iterating
#       through multiple lists at once:

electric = ["zapdos", "voltorb", "manectric", "pikachu"]
water = ["kyogre", "lapras", "squirtle", "goldeen"]
grass = ["budew", "bellsprout", "bulbasaur", "oddish"]

for electric_mon in electric:
    print(electric_mon)

for water_mon in water:
    print(water_mon)

for grass_mon in grass:
    print(grass_mon)

print()
# Not the best example, probably. But the first thing I could come up with.

# ====================================
# Doing More Work Within a for loop
# ====================================

# You can do just about anything with each item in a for loop. Let's build on the previous example by printing a message to each
# pokemon, telling them how hard they were to capture:

pokemon = ["articuno", "moltres", "zapdos"]
for mon in pokemon:
    print(f"{mon.title()}, it took me forever to get you to stay in that pokeball!")
print()

# This for loop works in the exact same way as it did above. Iterating through each mon in pokemon. The only differnce here
# is how we print the result. In this case, we are displaying each 'mon' in an f-string to write a message to them.

# NOTE: You can also write as many lines of code as you like in the for loop. Every indented line following the line 'for mon in pokemon:'
#      is considerd "inside the loop", and each indented line is executed once for each value in the list. Therefore, you can do as much
#      work as you like with each value in the list.

# pokemon = ["articuno", "moltres", "zapdos"]
# for mon in pokemon:
#     print(f"{mon.title()}, it took so long for me to catch you!")
#     print(f"I can't wait to try and catch other legendaries like you, {mon.title()}.\n")
# print()

# ===================================
# Doing something After a for loop
# ===================================

# If you want to end your program with something OUTSIDE the for loop, simply include the concluding block of code outside the for loop by
# no longer following the indentation pattern:

pokemon = ["articuno", "moltres", "zapdos"]
for mon in pokemon:
    print(f"{mon.title()}, it took so long for me to catch you!")
    print(f"I can't wait to try and catch other legendaries like you, {mon.title()}.\n")

print("Thank you, legendaries, for so much pokemon-catching fun!")
print()

# ==============================
# Avoiding Indentation Errors
# ==============================

# Python uses indentation to determine how a line, or group of lines, is related to the rest of the program. In the previous examples, the
# lines that printed messages to individual pokemon were part of the for loop because they were indented. Python's use of indentation makes
# the code very easy to read.  It's essentially forcing the use of whitespace to force you to write neatly formatted code with a clear visual structure.

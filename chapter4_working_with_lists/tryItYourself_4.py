# ==============
# 4-13. Buffet
# ==============

# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
menu = ("pizza", "burger", "pasta", "chicken", "steak")

# Use a for-loop to print each food the restaurant offers.
for food in menu:
    print(food)
print()

# Try to modify one of the items, and make sure that Python rejects the change.
# menu[1] = "lasagna"  >> confirmed this produces the Error that tuples don't accept item reassignment

# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple,
# and then use a for-loop to print each of the items on the revised menu.
menu = ("pizza", "burger", "pasta", "fish", "yogurt")
for food in menu:
    print(food)
print()

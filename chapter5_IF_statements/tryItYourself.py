# ========================
# 5.1 Conditional Tests
# ========================

list_to_choose_from = [
    "hitmonlee",
    "blaziken",
    "slaking",
    "metagross",
    "lantern",
    "gardevoir",
    "alakazam",
    "starmie",
    "gengar",
]

physical_atkr = ["hitmonlee", "blaziken", "slaking", "metagross"]
special_atkr = ["lantern", "gardevoir", "alakazam", "starmie", "gengar"]

print(list_to_choose_from)

user_pkmn_pick = input(
    "Name your favorite pokemon from the list and I'll tell you if it's a better physical attacker or a better special attacker: "
)
if user_pkmn_pick.lower() in list_to_choose_from:
    if user_pkmn_pick.lower() in physical_atkr:
        print("That pokemon is a physical attacker.")
    elif user_pkmn_pick.lower() in special_atkr:
        print("That pokemon is a special attacker, for sure.")
else:
    print("That pokemon is not the list I gave you. Tsk tsk.")


# We create a list of pokemon for the user to choose from.
# We create two more lists, splitting the first list into two more.
# Then we print() the first list so the user has a list to reference.
# We take the user's input and check if it is in the original list.
#   If TRUE, we then check to see if it's in the first list. If not, we check the second
#   list for it.
# If original test was FALSE, we tell them they did not choose a selection from our list
# we provided them.

# =============================
# 5.2 More Conditional Tests
# =============================

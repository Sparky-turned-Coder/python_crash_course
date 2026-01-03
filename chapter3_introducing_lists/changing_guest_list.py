guest_list = ["J.R.R. Tolkien", "Linus Torvaldi", "Walt Disney"]
print(guest_list)
print()

# print(
#     f"I would like to invite you, {guest_list[0]}, to dinner. I would hear of how you created such beautiful works of fantasy and your thought process behind it."
# )
# print(
#     f"I would like to invite you, {guest_list[1]}, to dinner. I'd like your advice for someone dabbling in the technical field and programming."
# )
# print(
#     f"I would like to invite you, {guest_list[2]}, to dinner. I'd love to pick your brain, learn how you remained so steadfast in the face of all that failure before succeeding."
# )

# ==============================
# NOTE: 3-5. Changing Guest List
# ==============================

# print(f"{guest_list[0]} will not be able to make it to dinner.\n")

guest_list[0] = "Jim Carrey"

# print(
#     f"I would like to invite you, {guest_list[0]}, to dinner. I'd love to discuss all the ups and downs your faced and how it made you better.\n"
# )
# print(
#     f"I would like to invite you, {guest_list[1]}, to dinner. I'd like your advice for someone dabbling in the technical field and programming.\n"
# )
# print(
#     f"I would like to invite you, {guest_list[2]}, to dinner. I'd love to pick your brain, learn how you remained so steadfast in the face of all that failure before succeeding.\n"
# )
# print()
#
# print(
#     "I would like to inform everyone that a larger table has been rounded up for us!\n"
# )

# =======================
# NOTE: 3-6. More Guests
# =======================
print(
    "I would like to inform everyone that a larger table has been rounded up for us!\n"
)


guest_list.insert(0, "Dad")
guest_list.insert(3, "Lyndsey")
guest_list.append("Kyle")

print(guest_list)
print()

print(
    f"I would like to invite you, {guest_list[0]}, to dinner. Just 'cause I love ya.\n"
)
print(
    f"I would like to invite you, {guest_list[1]}, to dinner. I'd love to discuss all the ups and downs your faced and how it made you better.\n"
)
print(
    f"I would like to invite you, {guest_list[2]}, to dinner. I'd like your advice for someone dabbling in the technical field and programming.\n"
)
print(
    f"I would like to invite you, {guest_list[3]}, to dinner. Just 'cause I love ya.\n"
)
print(
    f"I would like to invite you, {guest_list[4]}, to dinner. I'd love to discuss all the ups and downs your faced and how it made you better.\n"
)
print(f"I would like to invite you, {guest_list[5]}, to dinner. It's been a while.\n")
print()


# ===========================
# NOTE: Shrinking Guest List
# ===========================
print(guest_list)
print()
#  ['Dad', 'Jim Carrey', 'Linus Torvaldi', 'Lyndsey', 'Walt Disney', 'Kyle']

print(
    "As it turns out, my big fancy new table will not arrive on time. Alas, there is only space for two guests.\n"
)

first_removal = guest_list.pop(1)
print(f"I'm sorry, {first_removal}, but I'll have to vote you off the island. Thanks!")
print()

second_removal = guest_list.pop(1)
print(f"I'm sorry {second_removal}, but there's no room for you.")
print()

third_removal = guest_list.pop(2)
print(f"Sorry {third_removal}, but there's just no space for you here.")
print()

fourth_removal = guest_list.pop(2)
print(
    f"Sorry {fourth_removal}, but I can only have two here. We'll get together next time. ;)\n"
)
print()

print(
    f"By the way, {guest_list[0]}, you're still invited. As are you, {guest_list[1]}. :)"
)
print()

print("Dinner is over. It's been a pleasure, you two!")
del guest_list[0]
del guest_list[0]

print(f"Guests are now gone. Here's the empty list: {guest_list}.")
print()

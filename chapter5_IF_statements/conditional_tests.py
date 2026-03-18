# ===================
# Conditional Tests
# ===================

# A simple example:
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# NOTE At the heart of every if statement is an expression that can be evaluated as True or False.
#       This is called a "Conditional Test". Python uses the values True and False to decide whether
#       the code in an if statement should be executed. If a conidtional test evaluates to True, Python
#       executes the code following the if statement. If the test evaluates to False, Python ignores the
#       code following the if statement.

# NOTE Checking for Inequality

requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

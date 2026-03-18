# USING 'AND' TO CHECK MULTIPLE CONDITIONS

# To check whether two conditions are both True simultaneously, use the keyword 'and'
# to combine the two conditional tests; if each test passes, the overall expression
# evaluates to True.

# NOTE Therefore, 'and' conditionals require ALL statements to be TRUE for it to passes
#       the conditional test.

# >>> age_0 = 22
# >>> age_1 = 18
# >>> age_0 >= 21 and age_1 >= 21
#   False
# >>> age_1 = 22
# >>> age_0 >=21 and age_1 >= 21
#   True

# First we define two ages, age_0 and age_1.  Then we check whether both ages are 21
# or older.  The first test fails, since age_1 is not greater than or equal to 21.
# Using 'and', we need both tests to pass in order for this conditional test to be True.
# Therefore, FALSE.

# The second test passes, because we changed age_1 to equal '22', which is indeed
# greater than or equal to 21. Therefore, TRUE.

# To improve readability, we can use paranthesis around our statements, but it is not required.

age_0 = 22
age_1 = 18

print((age_0 >= 21) and (age_1 >= 21))
# This prints FALSE.
# Now, let's change age_1.

age_1 = 21

print((age_0 >= 21) and (age_1 >= 21))
# Now, this prints TRUE

# USING 'OR' TO CHECK MULTIPLE CONDITIONS

# The keyword 'or' allows you to check multiple conditions as well, but it passes when
# either or both of the individual tests pass. An 'or' expression fails ONLY when BOTH
# tests fail.


# >>> age_0 = 22
# >>> age_1 = 18
# >>> age_0 >= 21 and age_1 >= 21
#   TRUE
# >>> age_0 = 18
# >>> age_0 >=21 and age_1 >= 21
#   FALSE


age_2 = 22
age_3 = 18

print((age_2 >= 21) or (age_3 >= 21))
# TRUE, because at least one of the tests passes

age_2 = 18

print((age_2 >= 21) or (age_3 >= 21))
# FALSE, because neither test passes.

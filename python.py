# Notes

# Python is a zero based language! [0] = the first item.

# Variable  notes


# \n = new line
# \" = puts " in without breaking string
# len(variable_name) = variable_name.length()
# .replace("old str", "new str") = replaces strings

# Number notes

# abs(num) = absolute value
# pow(num, exponent) = exponents
# from ___ import * = imports everything from a library, such as math

# List notes

# num = [2, 3, 4] num[-1] = 4. num[-2] = 3. Negative index starts from the last item going backward.
# [1:] = all list items starting from the second one. [1:4] All items from the second to, but not including, the fifth.
# .extend() adds a list to the end of your current list. Ex. num.extend(people) = [2, 3, 4, "Derek", "Sam", "Jake"]
# .append() adds one value to the end of your current list. Ex num.append(5) = [2, 3, 4, 5]
# .insert() takes 2 values.The index you want your new value to be in, and the new value. Ex num.insert(2,9) = [2,3,9,4]
# .remove() removes a value that you put in. Not index of the value, the value itself!
# .clear() clears a list.
# .pop() pops the last value out of a list.
# .index() finds the index of a value. Value isn't in list? Error!
# .count() counts how much values are inside the list.
# .sort() sorts values in an array by alphabetical order if they're words, and ascending order if numbers. Both = error
# .copy() creates a list copy
# Tuples are like lists, but cannot change!

# Function notes

# Function code is indented. Stop indenting and you're not in that function anymore.
# Parameters are same as JS
# Return is same as JS

# If statements

# Ifs are very similar in Python to JS. Instead of {}, it's : Indented code is also in use for ifs. else is not indented
# Elif (py) is the same as else if (js)

# Lists

people = ["Derek", "Sam", "Jake"]

people.sort()
print(people)

# Functions

def sayhi():
    print("Hello")

sayhi()

# If statements

is_yummy = False
is_healthy = True

if is_yummy and is_healthy:
    print("This is the best food!")
elif is_yummy and not(is_healthy):
    print("This is yummy but isn't good for me.")
elif is_healthy and not(is_yummy):
    print("This is healthy but tastes bad.")
else:
    print("This food is terrible.")

# For statements

for index in range(4, 27):
    if index == 4:
        print("It's the first!")
    elif index == 26:
        print("Last but definitely not least!")
    else:
        print(index)

# Exponent function

def exponent(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(exponent(3,2))

# 2D lists

stuff_for_me = [
    ["wake up", "make bed", "eat breakfast", "brush teeth"],
    ["Do learning", "Play", "Eat lunch", "Play or code"],
    ["Eat dinner", "(possibly) watch movie and eat snacks", "brush teeth", "sleep"]
]



for row in stuff_for_me:
    for thing_to_do in row:
        print(thing_to_do)
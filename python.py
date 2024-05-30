from Computer import Computer


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
elif is_yummy and not is_healthy:
    print("This is yummy but isn't good for me.")
elif is_healthy and not is_yummy:
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
    for i in range(pow_num):
        result = result * base_num
    return result


print(exponent(3, 2))

# 2D lists

stuff_for_me = [
    ["wake up", "make bed", "eat breakfast", "brush teeth"],
    ["Do learning", "Play", "Eat lunch", "Play or code"],
    ["Eat dinner", "(possibly) watch movie and eat snacks", "brush teeth", "sleep"]
]


for row in stuff_for_me:
    for thing_to_do in row:
        print(thing_to_do)

# Translation practice


def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "ZZ"
            else:
                translation = translation + "zz"
        else:
            translation = translation + letter
    return translation


print(translator("bounce"))

# Try and except (catches errors)

# try:
#     user_in = int(input("Type in something that's a number: "))
#     print(f"{user_in} is a very cool number")
# except ValueError as err:
#     print(f"How dare you {err}!")

# Read other files

notes = open("notes.txt", "a")

notes.write("\n This is with the power of PYTHON!")

notes.close()


# Classes + objects

computer = Computer("YOGA", 2, 512, 16)
computer2 = Computer("Dell", 3, 1024, 16)

myComputer = computer

myComputer.turn_on()
print(computer2.ssd)
print(computer2.is_big_computer())

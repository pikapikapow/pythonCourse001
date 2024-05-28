guess_counter = 0
guess_limit = 5
secret_word = "secret"
are_u_out = False
guess = ""

while guess != secret_word and not(are_u_out):
    if guess_counter < guess_limit:
        guess = input("Enter your guess:")
        guess_counter += 1
    else:
        are_u_out = True

if are_u_out:
    print("Sorry, but you have LOST!")
else:
    print("You have won! Yippee!")
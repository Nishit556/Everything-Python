import random
n = 20
to_be_guessed = (int(n * random.random())) + 1
guess = 0
while guess != to_be_guessed:
    guess = int (input("New Number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number is to large.")
        elif guess < to_be_guessed:
            print("NUmber is too small")
    else:
        print("So you are giving up huh!")
        break
else:
    print("You Won my nigga!")




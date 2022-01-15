secret_number = 9
guess_count = 0
guess_limit = int(input('guess_limit: '))
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won Mah Niggahhh!!!!! #TNA #AEW #WWE #NJPW")
        break
else:
    print("You lost asshole. Now sit down and shut your fucking mouth")
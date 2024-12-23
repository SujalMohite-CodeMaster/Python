secret_number = 9

Guess_count = 0
guess_limit = 3
while Guess_count < guess_limit:
    guess = int(input("Guess: "))
    Guess_count += 1
    if guess == secret_number:
        print("You guess corrected")
        break
else:
    print("Sorry you're failed. ")

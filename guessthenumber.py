import random
num = (1,2,3,4,5,6,7,8,9,10)
Secerte_Number=random.choice(num)

guess_limit = 3
guess_count = 1

while guess_count<=guess_limit:
    guess = int(input("Enter your guess > "))
    if guess==Secerte_Number:
        print("Congrtulations! You guess the Correct number.")
    else:
        print("Wrong guess, Try again.")
    guess_count += 1
        
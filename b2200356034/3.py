import random

number = random.randint(1,26)
guess = int(input("guess a number between 1 adn 25: "))
game = True
while game:
    if number == guess:
        print("correct")
        game = False
    else:
        if guess > number:
            print("decrease your guess")
            guess = int(input("guess a number: "))
        else:
            print("increase your guess")
            guess = int(input("guess a number: "))

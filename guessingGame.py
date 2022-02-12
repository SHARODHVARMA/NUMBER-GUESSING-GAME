import random
print("Number Guessing Game")
number = random.randint(1,9)
#print(number)
chances = 0
print("Guess a number between 1 and 9: ")

while chances < 5 :
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("YOU WIN!")
        break
    elif guess < number:
        print("Your guess is low")
    else:
        print("Your guess is high")
    chances = chances+1
if not chances < 5:
    print("YOU LOSE! The number is", number)
    

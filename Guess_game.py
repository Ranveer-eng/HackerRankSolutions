import random
num = int(random.randint(0,10))
guess_it = False

while not guess_it:
    guess = int(input("Guess a number between 0 to 10: "))
    guess_it = num == guess
    
print("Well Done!")

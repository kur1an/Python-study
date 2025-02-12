import random

num = random.randint(1, 100)  # Random number between 1 and 100

try:
    a = int(input("Guess a number: "))  # Convert input to an integer
    
    if a < num:
        print("Too low!")
    elif a > num:
        print("Too high!")
    else:
        print(a, "is the guessed number. You got it right!")
        
except ValueError:
    print("Not a valid input! Please enter an integer.")

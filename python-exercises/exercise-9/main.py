#Guessing Game v1

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random

random_number = random.randint(1, 9)

is_running = True
number_guess = 0

while is_running:
    
    user_input = input("Guess the number: 1 - 9 : ").lower()
    if user_input == "exit":
        is_running = False
    else:
        if random_number == int(user_input):
            print("Exactly right!")
            print(f"Number of guess: {number_guess}")
            is_running = False
        else:
            if random_number > int(user_input):
                print("Too low")
                number_guess += 1
            else:
                print("Too high")
                number_guess += 1




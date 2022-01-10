# Cows And Bulls   
# Exercise 18 (and Solution)
# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to GUESS a 4-digit number. For every digit that the user GUESSed correctly in the correct place, they have a “cow”. For every digit the user GUESSed correctly in the wrong place is a “bull.” Every time the user makes a GUESS, tell them how many “cows” and “bulls” they have. Once the user GUESSes the correct number, the game is over. Keep track of the number of GUESSes the user makes throughout teh game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:

#   Welcome to the Cows and Bulls Game! 
#   Enter a number: 
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
# Until the user GUESSes the number.

import random

GUESS = 1

def generate_number():
    random_number = random.randint(1000, 9999)
    
    return random_number

def check_number(num, rnum):
    num_list = list(num)
    rnum_list = list(rnum)
  
    c = 0
    b = 0
    global GUESS
    global is_running
    for x in range(0, 4):
        if num_list[x] == rnum_list[x]:
            c += 1
        else:
            b += 1
    print(f"{c} cows, {b} bulls {GUESS} guess")

    if c >= 4:
        print(f"You win!!\nYou guessed for {GUESS} times :D")
        is_running = False
    else:
        GUESS += 1

random_number = str(generate_number())
print(random_number)
print("Welcome to the Cows and Bulls Game! ")

is_running = True

while is_running:
    user_input = input("Enter a 4 digit number :")

    if len(user_input) == 4:
        check_number(num=user_input, rnum=random_number)
    else:
        print("Please enter 4 digit number.")



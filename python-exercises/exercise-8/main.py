# Rock Paper Scissors   
# Exercise 8 (and Solution)
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock
is_running = True

while is_running:
    print("Rock Paper Scissors\n")
    player_1 = input("Player 1: ").lower()
    if player_1 == "quit":
        is_running = False
    else:
        print("----------------------")
        print("----------------------")
        print("----------------------")
        print("----------------------")

        player_2 = input("Player 2: ").lower()
        if player_2 == "quit":
            is_running = False
        else:
            print("----------------------")
            print("----------------------")
            print("----------------------")
            print("----------------------")

            if player_1 == "rock" and player_2 == "scissors":
                print("Player 1 WINS!")
            if player_1 == "scissors" and player_2 == "paper":
                print("Player 1 WINS!")
            if player_1 == "paper" and player_2 == "rock":
                print("Player 1 WINS!")

            if player_2 == "rock" and player_1 == "scissors":
                print("Player 2 WINS!")
            if player_2 == "scissors" and player_1 == "paper":
                print("Player 2 WINS!")
            if player_2 == "paper" and player_1 == "rock":
                print("Player 2 WINS!")

            if player_2 == "rock" and player_1 == "rock":
                print("It's a draw!")
            if player_2 == "scissors" and player_1 == "scissors":
                print("It's a draw!")
            if player_2 == "paper" and player_1 == "paper":
                print("It's a draw!")

    
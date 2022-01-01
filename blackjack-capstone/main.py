############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo

import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_start = "y"
while game_start == "y":
  game_start = input("Do you want to play a game of BlackJack? Type 'y' to start or 'n' end the game. \n")

  def lets_play():
    run_game = True
    
    player_cards = []
    computer_cards = []

    player_score = 0
    computer_score = 0


    def give_card_player(player):
      player.append(random.choice(cards))
      return player

    def give_card_computer(computer):
      computer.append(random.choice(cards))
      return computer



    #game start
    for start in range(0,2):
      give_card_player(player_cards)
      give_card_computer(computer_cards)

    def show_cards(final):
      if final == False:
        player_score = sum(player_cards)
        computer_score = sum(computer_cards)
        print(f"\n\nYour cards: {player_cards}, current score: {player_score}")
        print(f"Dealer card: {computer_cards[0]}")
        #print(f"Dealer score: {computer_score}")
      else:
        player_score = sum(player_cards)
        computer_score = sum(computer_cards)
        print(f"\n\nYour final cards: {player_cards}")
        print(f"Dealer final cards: {computer_cards}")
        print(f"Your score: {player_score}")
        print(f"Dealer score: {computer_score}")
    show_cards(False)

    while run_game == True:
      player_score = sum(player_cards)
      computer_score = sum(computer_cards)
      if player_score > 21:
        print("You lose!")
        run_game = False
      else:
        another_card = input("\n\nType 'y' for another card, 'n' to pass.").lower()

        if another_card == "y":
          #player_cards.append(random.choice(cards))
          give_card_player(player = player_cards)
          if computer_score < 17:
            give_card_computer(computer = computer_cards)
          show_cards(False)
        elif another_card == "n":
          if player_score > computer_score:
            show_cards(True)
            print("You win!")
            run_game = False
          elif player_score == computer_score:
            show_cards(True)
            print("Its a draw!")
          elif computer_score > 21 and player_score <= 21:
            show_cards(True)
            print("You win!")
          else:
            show_cards(True)
            print("You lose!")
            run_game = False
        else:
          print("That's not an option")

  if game_start == "y":
    lets_play()
print("Game Ended! Please close the game now.")

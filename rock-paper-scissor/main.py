import random

rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
print("Welcome to my Python's Rock Paper Scissors Game!\n\n")


myHand = int(input("Type 0 for Rock\nType 1 for Paper,\nType 2 for Scissors\n"))

if myHand >= 3:
  print("Sorry that's not a choice!")
else:

  if myHand == 0:
    print(f"\n\nYou chose Rock!\n")
    print(game_images[myHand])
  elif myHand == 1:
    print(f"\n\nYou chose Paper!\n")
    print(game_images[myHand])
  elif myHand == 2:
    print(f"\n\nYou chose Scissors!\n")
    print(game_images[myHand])


  compHand = random.randint(0, 2)

  print(compHand)

  if compHand == 0:
    print(f"\n\nAI chose Rock!\n")
    print(game_images[compHand])
  elif compHand == 1:
    print(f"\n\nAI chose Paper!\n")
    print(game_images[compHand])
  elif compHand == 2:
    print(f"\n\nAI chose Scissors!\n")
    print(game_images[compHand])

  win = f"Congratulations! You win!!"
  lose = f"Sorry you lose, try again!"
  draw = f"It's a draw!"

  #RULES
  #for your rock
  if myHand == 0 and compHand == 2:
    print(win)
  elif myHand == 0 and compHand == 1:
    print(lose)
  elif myHand == 0 and compHand == 0:
    print(draw)
  #for your paper
  elif myHand == 1 and compHand == 2:
    print(lose)
  elif myHand == 1 and compHand == 1:
    print(draw)
  elif myHand == 1 and compHand == 0:
    print(win)
  #for your scissor
  elif myHand == 2 and compHand == 2:
    print(draw)
  elif myHand == 2 and compHand == 1:
    print(win)
  elif myHand == 2 and compHand == 0:
    print(lose)

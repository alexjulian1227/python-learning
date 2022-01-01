import random
import hangman_art
import hangman_dictionary
#you can also modify calling the variables inside the module by using the code below
#from hangman_dictionary import word_list(variable)
#after this you can easily type in word_list directly

print(hangman_art.logo)

#randomly choose a word from the list
#input user guess letter
#check if the user guess is within the generated word

#create empty list called display
#for each in random word add a "_" to display
#loop through each and if the guess letter matches the one of display then show replace "_" with the corresponding guess guess_letter
#print display and you should see the guessed letter switched over to the display "c" "_" "_"......


random_word = random.choice(hangman_dictionary.word_list)
#print(random_word)

display = []
correct_letters = []
wrong_letters = []

 
len_random_word = len(random_word)

for n in range(len_random_word):
  display += "_"

lives = 6
blank_letters = 10
print(hangman_art.stages[6])

rules = False

while not rules:
  
  #you can also use in this while condition
  #while not end_of_game
  #end_of_game = false
  # if "_" not in display list
  #   end_of_game = True

  guess_letter = input("Guess a letter: ").lower()
  #print(len(random_word))
  #print(display)
  
  
  if guess_letter in random_word:

    for position in range(len_random_word):
      letter = random_word[position]
      if letter == guess_letter:
        display[position] = letter
    correct_letters.append(guess_letter)
    print(f"You guessed the letter {guess_letter}! Choose another one.")
  
  else:
     print(f"Sorry {guess_letter} is not included in the word. You lose a life!. You only have {lives} left.")
     lives -= 1
     wrong_letters.append(guess_letter)
     print(hangman_art.stages[lives])
     
      
  print(f"Correct letters: {', '.join(correct_letters)}")
  print(f"Missed letters: {', '.join(wrong_letters)}")  
  blank_letters = display.count("_")

  if blank_letters == 0:
    rules = True
    endgame_msg = ("\n\nCongratulations! You guessed the word!")
  elif lives == 0:
    rules = True
    print(f"The word is {random_word}")
    endgame_msg = ("\n\nYou are hanged!!!!!")
  #removing the list " " in the output using join function
  print(f"{' '.join(display)}")

print(endgame_msg)

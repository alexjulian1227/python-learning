from art import logo

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(logo)
# def encrypt(etext,eshift):
#   cipher_text = ""
#   for letter in etext:
#     position = alphabet.index(letter)
#     new_position = position + eshift
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encrypted word is {cipher_text}")

# def decrypt(etext, eshift):
#   cipher_text = ""
#   for letter in etext:
#     position = alphabet.index(letter)
#     new_position = position - eshift
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The decrypted word is {cipher_text}")

#function caesar is a combination of the above codes for code organization
def caesar(etext, eshift, edirection):
  cipher_text = ""
  for char in etext:
    if char in alphabet:
      position = alphabet.index(char)
      if edirection == "encode":
        new_position = position + eshift
        output_message = "encrypted"
      elif edirection == "decode":
        new_position = position - eshift
        output_message = "decrypted"
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    else:
      cipher_text += char
  print(f"The {output_message} word is {cipher_text}")


is_run = True





while is_run == True:

  direction =   input("Type 'encode' to encrypt, type  'decode' to decrypt.\n")

  text = input("Type your message:\n").lower()

  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  #print(shift)

  # if direction == "encode":
  #   encrypt(etext = text, eshift = shift)
  # else:
  #   decrypt(etext = text, eshift = shift)

  caesar(etext = text, eshift = shift, edirection = direction)

  run = input("\n\nWould you like to run the program again?\nType yes or no.\n").lower()


  if run == "no":
    is_run = False
    print(f"Thank you for using the Caesar Cipher!")
  elif run == "yes":
    is_run = True
    
  else:
    print(f"That's not a choice please run the program again.") 

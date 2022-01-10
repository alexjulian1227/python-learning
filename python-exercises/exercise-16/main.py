# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random
import string


def weak_password():
    list_password = ["!Mypass2811", "$Random17", "@Self222", "#Modern092", "!Vivacious12", "!Obeisant544"]

    random_pass = random.choice(list_password)
    
    return random_pass

def strong_password():
    alphabet_list_lowercase = list(string.ascii_lowercase)
    alphabet_list_uppercase = list(string.ascii_uppercase)
    numeric_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbol_list = ["!", "@", "#", "$"]

    # 5 alpha 3 numeric 1 symbol
    
    generate_alpha_lowercase = ''.join([random.choice(alphabet_list_lowercase) for x in range(0, 4)])

    generate_alpha_uppercase = ''.join([random.choice(alphabet_list_uppercase) for x in range(0, 1)])
    
    generate_number = ''.join([str(random.choice(numeric_list)) for x in range(0, 2)])

    generate_symbol = random.choice(symbol_list)

    alpha = f"{generate_alpha_lowercase}{generate_alpha_uppercase}{generate_number}{generate_symbol}"
    password = list(alpha)
    
    for i in range(len(password)-1, 0, -1):
     
        # Pick a random index from 0 to i
        j = random.randint(0, i + 1)
    
        # Swap arr[i] with the element at random index
        password[i], password[j] = password[j], password[i]
    new_pass = ''.join(password)
    return new_pass
    

user_input = input("Type 'strong' or 'weak' for your password: ").lower()

if user_input == "strong":
    print(f"Here's your strong password: {strong_password()}")
else:
    print(weak_password())
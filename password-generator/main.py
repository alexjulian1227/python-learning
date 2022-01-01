#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



#counting the data in the list

count_letters = len(letters)
count_symbols = len(symbols)
count_numbers = len(numbers)

#generating random output from list
random_letter = []
for n in range(0, nr_letters):
  n = letters[random.randint(0, count_letters) - 1]
  random_letter.append(n)
  

random_symbol = []
for n in range(0, nr_symbols):
  n = symbols[random.randint(0, count_symbols) - 1]
  random_symbol.append(n)

random_number = []
for n in range(0, nr_numbers):
  n = numbers[random.randint(0, count_numbers) - 1]
  random_number.append(n)

#line by line check
# print(random_letter)
# print(random_symbol)
# print(random_number)

#converting list obj to string
str_letter = ''.join(map(str, random_letter))
str_symbol = ''.join(map(str, random_symbol))
str_number = ''.join(map(str, random_number))


#line by line check
# print(str_letter)
# print(str_symbol)
# print(str_number)

#easy level
str_password = str_letter + str_symbol + str_number
print(f"\n\nYour randomized password is: {str_password}")


#hard level
#random without sequence :D
str_len = (len(str_password))

str_password = ''.join(random.sample(str_password,str_len))

print(f"\n\nYour randomized password is: {str_password}")

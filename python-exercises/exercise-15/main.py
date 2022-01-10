# Exercise 15 (and Solution)
# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.

user_input = input("Enter a sentence or phrase and the code will post it in reverse order : ")

def reverse_order(text):
    list_string = text.split()
    return print(list_string[::-1])


reverse_order(user_input)
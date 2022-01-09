# Exercise 12 (and Solution)
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the 
# first and last elements of the given list. 
# For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]

a_count = len(a)

def first_last(list):
    new_list = [x for x in list[0: a_count: a_count - 1]]
    print(new_list)
    
print(a)
first_last(a)

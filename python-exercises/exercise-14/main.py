# List Remove Duplicates  
# Exercise 14 (and Solution)
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list 
# minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

list_a = [1,3,3,6,5,4,3,3,2,2,1,2,5,6,7,8,9,8,6,5,4,3]
#[z[i] for i in range(len(z)) if i == z.index(z[i])] list comprehension for dups
def remove_duplicates_list(lists):
    
    new_list = [lists[i] for i in range(len(lists)) if i == lists.index(lists[i])]
    return print(new_list)

def remove_duplicates_set(lists):

    new_set = set(lists[i] for i in range(len(lists)) if i == lists.index(lists[i]))
    return print(new_set)

    
remove_duplicates_list(list_a)
remove_duplicates_set(list_a)

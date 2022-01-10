# Exercise 20 (and Solution)
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

my_list = range(1, 101)

def search_number(num):
    if num in my_list:
        return True
    else:
        return False


def search_binary(num):
    start_index = 1
    end_index = len(my_list) - 1

    while True:
        middle_index = (end_index - start_index) / 2

        if middle_index < start_index or middle_index > end_index or middle_index < 0:
            return False
        
        middle_element = my_list[middle_index]

        if middle_element == num:
            return True
        elif middle_element < num:
            end_index = middle_index
        else:
            start_index = middle_index

user_input = int(input("Enter a number to search :"))

print(search_binary(user_input))


user_input = input("Enter a text and ill check if it's palindrome or not. ")

string_list = list(user_input)

reverse_string = string_list[::-1] #slicing 

count_list = len(string_list)

palindrome = 0
for x in range(0, count_list):
    if string_list[x] == reverse_string[x]:
        palindrome += 1

if palindrome == count_list:
    print("It's a palindrome.")
else:
    print("It's not")



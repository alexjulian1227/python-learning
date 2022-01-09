
user_number = int(input("Enter a number: "))
user_number_2 = int(input("Enter another number: "))

result = user_number / user_number_2

if result % user_number_2 == 0:
    print("That's a perfect combination")
else:
    print("Numbers not match")

if user_number % 4 == 0:
    print("This number is divisible by 4.")
else:
    if user_number % 2 == 0:
        print("Your first number is even.")
    else:
        print("Your number is odd.")
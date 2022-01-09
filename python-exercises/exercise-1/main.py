user = input("What is your name?")
age = int(input("How old are you?"))
number = int(input("Enter a number:"))
years_left = (100 - age) + 2022

for x in range(0, number):
    print(f"Hi {user}, you will turn 100 years old on {years_left}")

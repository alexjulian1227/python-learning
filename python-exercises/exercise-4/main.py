
x = range(2, 101)


user_input = int(input("Enter a number and Ill provide the divisor for that number. "))

for num in x:
    if user_input % num == 0:
        print(f"{num} is a divisor of {user_input}")



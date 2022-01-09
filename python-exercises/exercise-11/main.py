x = range(1, 101)


def prime_number(num):
    prime_count = 0
    for lists in x:
        if num % lists == 0:
            prime_count +=1
            
    if prime_count > 2:
        print("Not a prime number")
    else:
        print("This is a prime number!")
user_input = int(input("Enter a number: "))


prime_number(user_input)

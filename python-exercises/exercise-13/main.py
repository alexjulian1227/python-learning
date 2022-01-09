# Fibonacci  
# Exercise 13 (and Solution)
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
x = 1
y = 1
c = f"{x},{y}"

user_input = int(input("How long is your fibonacci sequence? :"))

def fibonacci(long):
    global x, y, c
    for count in range(1, long - 1):
        sum = x + y
        c = f"{c},{sum}"
        
        x = y
        y = sum
    print(c)    
    
fibonacci(user_input)
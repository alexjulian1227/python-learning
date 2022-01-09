
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in a:
    if x < 5:
        print(f"{x} is less than 5")
    
new_a = [x for x in a if x < 5]

print(new_a)

new_input = int(input("Enter a number and Ill return all the numbers below that."))

for x in a:
    if x < new_input:
        print(f"{x} is less than {new_input}")




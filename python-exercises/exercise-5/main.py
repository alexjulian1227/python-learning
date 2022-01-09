a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = list(dict.fromkeys(a)) #remove duplicates inside a list

for x in range(0, len(c)) :
    if c[x] in b:
        print(f"{c[x]} is in List B")
    else:
        print(f"{c[x]} is not in List B")




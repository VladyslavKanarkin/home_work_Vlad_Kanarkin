number = [1, 2, 3, 4, 5, 7, 8]

i = number[0]
for x in number:
    if x != i:
        print(x)
        break
    i += 1

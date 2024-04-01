numbers = [1, 3, 6, 8, 11, 34, 55, 64, 88, 112, 117]
number = int(input("Enter divider:"))
for i in numbers:
    if i % number == 0:
        print(i)

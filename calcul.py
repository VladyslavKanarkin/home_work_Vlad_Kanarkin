operation = input("Вибір операції: '+', '-', '*', '/'")

number_1 = int(input('Перша цифра: '))
number_2 = int(input('Друга цифра: '))
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

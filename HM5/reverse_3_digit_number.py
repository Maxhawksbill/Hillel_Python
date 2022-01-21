number = input('Type any number that equal or greater than 100:')
number = int(number)
if number // 100 == 0:
    print('Please, enter equal or greater then 100!')
else:
    digit1 = number // 100
    digit2 = (number // 10) % 10
    digit3 = (number % 100) % 10
    number = digit3 * 100 + digit2 * 10 + digit1
    print(number, type(number))

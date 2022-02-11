def arithmetic(number1, number2, action):
    action = tuple(action)
    if number2 == 0 and action == ('/', ):
        return "Division by zero"
    d = {('+',): number1 + number2,
         ('-',): number1 - number2,
         ('*',): number1 * number2,
         ('/',): number1 / number2
         }
    if action not in d.keys():
        return "Unknown operation"
    else:
        value = d.get(action)
    return f'The result of the operation: {value}'


x = int(input('Type 1st number: '))
y = int(input('Type 2d number: '))
to_do = input('Type the math action (e.g., +, -, /, *): ')
print(arithmetic(x, y, to_do))

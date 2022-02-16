def arithmetic(number1, number2, action):
    value = 0
    if number2 == 0 and action == '/':
        return "Division by zero"
    if action != '+' and action != '-' and action != '/' and action != '*':
        return f"Unknown operation {action}"
    if action == '+':
        value = number1 + number2
    elif action == '-':
        value = number1 - number2
    elif action == '*':
        value = number1 * number2
    else:
        value = number1 / number2
    return round(value, 2)


x = int(input('Type 1st number: '))
y = int(input('Type 2d number: '))
to_do = input('Type the math action (e.g., +, -, /, *): ')
print(f'The result of the operation: {arithmetic(x, y, to_do)}')

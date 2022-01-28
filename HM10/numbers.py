qty = 0
sum = 0
average = 0
odds = 0
evens = 0
numbers = []
while True:
    val = int(input('Enter an integer number:'))
    numbers.insert(0, val)
    if val == 0:
        break
    qty = qty + 1
    sum = sum + val
    average = sum / qty
    if (val % 2) == 0:
        evens = evens + 1
    else:
        odds = odds + 1
    for _ in numbers:
        maximum = max(numbers)
        minimum = min(numbers)
print('Quantity of numbers: ' + str(int(qty)) + '\n'
        'Sum of numbers: ' + str(int(sum)) + '\n'
        'Average of numbers: ' + str(average) + '\n'
        'Maximum from numbers: ' + str(int(maximum)) + '\n'
        'Minimum from numbers: ' + str(int(minimum)) + '\n'
        'Quantity of odd numbers: ' + str(int(odds)) + '\n'
        'Quantity of even numbers: ' + str(int(evens)))
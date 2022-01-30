first_val = int(input('Enter an integer number:'))
if first_val == 0:
    exit(0)
qty = 1
sum = first_val
average = first_val
odds = 0
evens = 0
if (first_val % 2) == 0:
    evens = evens + 1
else:
    odds = odds + 1
prev_val = first_val
maximum = minimum = first_val
while True:
    val = int(input('Enter an integer number:'))
    if val == 0:
        break
    qty = qty + 1
    sum = sum + val
    average = sum / qty
    if (val % 2) == 0:
        evens = evens + 1
    else:
        odds = odds + 1
    maximum = max(prev_val, val, first_val)
    minimum = min(prev_val, val, first_val)
    prev_val = val
print('Quantity of numbers: ' + str(int(qty)) + '\n'
    'Sum of numbers: ' + str(int(sum)) + '\n'
    'Average of numbers: ' + str(average) + '\n'
    'Maximum from numbers: ' + str(int(maximum)) + '\n'
    'Minimum from numbers: ' + str(int(minimum)) + '\n'
    'Quantity of odd numbers: ' + str(int(odds)) + '\n'
    'Quantity of even numbers: ' + str(int(evens)))
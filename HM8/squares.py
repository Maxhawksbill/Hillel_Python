a = int(input('Enter an integer N:'))
while a == 0:
    a = int(input('Enter greater than zero!\n'
              'Enter an integer N:'))
    if a == 0:
        continue
if a == 1:
    print(a)
i = 1
while i**2 < a:
    print(i**2, end=' ')
    i = i + 1

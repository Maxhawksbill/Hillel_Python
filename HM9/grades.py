a = int(input('Enter an integer N:'))
while a == 0:
    a = int(input('Enter greater than zero!\n'
              'Enter an integer N:'))
    if a == 0:
        continue
i = 1
t = 0
while i < a:
    i = i * 2
    t = t + 1
    if i*2 > a:
        break
print(t, i)
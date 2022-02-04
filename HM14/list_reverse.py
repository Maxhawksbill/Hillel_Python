s = input('Enter through the space button a list of integer numbers:')
lst = list(s.split(' '))
i = 1
for _ in lst:
    print(lst[len(lst) - i], end=' ')
    i = i + 1
lst = list(input('Enter a list of integer numbers:'))
i = 1
for _ in lst:
    print(lst[len(lst) - i], end=' ')
    i = i + 1
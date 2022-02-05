s = input('Enter through the space button a list of integer numbers:')
lst = list(s.split(' '))
for i in range(0, len(lst) // 2):
    lst.append(lst[i])
    lst[i] = lst[len(lst) - 2 - i]
    lst[len(lst)- 2 - i] = lst[len(lst) - 1]
    lst.pop()
print(lst)
s = input('Enter through the space button a list of integer numbers:')
lst = list(s.split(' '))
"""s = len(lst)
lst.extend(lst[::-1])
del lst[0: s]"""
for i in range(len(lst) // 2):
    lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]
print(lst)
from random import randint

lst = [randint(1, 10) for _ in range(5)]
print(lst)
ind = int(input('Enter an index from this list: '))
i = 0
for i in range(ind, len(lst) - 1):
    lst[i] = lst[i + 1]
lst.pop()
print(lst)

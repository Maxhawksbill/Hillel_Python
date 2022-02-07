from random import randint

lst1 = [randint(1, 100) for _ in range(10)]
lst2 = [randint(1, 100) for _ in range(10)]
print(lst1)
print(lst2)
print('In these lists there is (are):', len(set(lst1 + lst2)), ' unique item (s)')
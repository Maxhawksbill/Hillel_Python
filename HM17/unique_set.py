from random import randint

lst = [randint(1, 100) for _ in range(10)]
print(lst)
print('In this list there is (are):', len(set(lst)), ' unique item (s)')
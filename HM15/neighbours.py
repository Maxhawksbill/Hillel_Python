s = input('Enter through the space button a list of integer numbers:')
lst = list(s.split(' '))
t = 0
for i in range(1, len(lst) - 1):
    if (int(lst[i]) > int(lst[i -1])) and (int(lst[i]) > int(lst[i + 1])):
        t = t + 1
    else:
        continue
print("The quantity of numbers which are greater than their neighbors is: " + str(t))
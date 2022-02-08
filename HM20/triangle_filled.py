height = int(input('Enter the height of the triangle: '))
a = height // 4
side = int((3 ** 0.5) * height) + a
for i in range(height):
    for j in range(side):
        if j == side // 2 - i:
            print('* ' * (2 * i + 1), end='')
        else:
            print('  ', end='')
    print()
print()
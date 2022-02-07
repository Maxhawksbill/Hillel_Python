height = int(input('Enter the height of the triangle:'))
side = int((3 ** 0.5) * height)
for i in range(height):
    for j in range(side + 1):
        if j == (side // 2) - i or j == (side // 2) + i or \
                 i == height - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()

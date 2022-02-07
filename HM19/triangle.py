height = int(input('Enter the height of the triangle: '))
side = int((3 ** 0.5) * height)
if 8 > height >= 4:
    side += 1
elif height >= 8:
    side += 2
for i in range(height):
    for j in range(side):
        if abs(j - (side // 2)) == i or i == height - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()

def square(side):
    side = int(side)
    perimeter = side * 4
    sqr = side ** 2
    dgl = (2 * side ** 2) ** 0.5
    return perimeter, sqr, dgl


x, y, z = square(input('Enter the side of the square to know it\'s perimeter, area and diagonal: '))
print(f'Perimeter of the square: {x}\n'
      f'Area of the square: {y}\n'
      f'Diagonal of the square: {round(z, 2)}')

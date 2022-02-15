def square(side):
    side = int(side)
    perimeter = side * 4
    sqr = side ** 2
    dgl = (2 * side ** 2) ** 0.5
    return f"Perimeter of the square: {perimeter}\n" \
           f"Area of the square: {sqr}\n" \
           f"Diagonal of the square: {round(dgl, 2)}"


print(square(input('Enter the side of the square to know it\'s perimeter, area and diagonal: ')))

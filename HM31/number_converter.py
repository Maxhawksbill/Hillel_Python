from string import ascii_uppercase


def number_converter(number, scale=2):
    number, scale = int(number), int(scale)
    num_conv = []
    res = ''
    while number > 0:
        num_conv += [str(number % scale) if number % scale in range(0, 10) else ascii_uppercase[number % scale - 10]]
        number = number // scale
    for i in num_conv[::-1]:
        res += i
    return res


print(number_converter(input("Enter a number to convert: "), input("Enter a scale to convert to: ")))


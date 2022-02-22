dict = {key: chr(key) for key in range(32, 127)}


def symbol(sym_number):
    sym_number = int(sym_number)
    return dict.get(sym_number)


print(symbol(input("Enter a number in interval from 32 to 127 included: ")))
print(dict)

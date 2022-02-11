def leap_year(year):
    year = int(year)
    if year % 4 != 0:
        return False #f"{str(year)} is not a leap year!"
    elif year % 100 == 0 and year % 400 != 0:
        return False #f"{str(year)} is not a leap year!"
    else:
        return True #f"{str(year)} is a leap year!"


print(leap_year(input('Type any year to check if it is leap:')))
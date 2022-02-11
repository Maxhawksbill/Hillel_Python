def season(month):
    month = int(month)
    d = dict(winter=[1, 2, 12],
             spring=[3, 4, 5],
             summer=[6, 7, 8],
             autumn=[9, 10, 11]
             )
    if month not in d.values():
        return "This number is out of the month's range"
    cur_season = [cur_season for cur_season in d.keys() if month in d[cur_season]][0].capitalize()
    return f"Current season is: {cur_season}"


print(season(input('Type the current month in range from 1 to 12: ')))

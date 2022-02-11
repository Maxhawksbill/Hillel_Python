def season(month):
    month = int(month)
    d = dict(winter=[1, 2, 12],
             spring=[3, 4, 5],
             summer=[6, 7, 8],
             autumn=[9, 10, 11]
             )
    cur_season = [cur_season for cur_season, cur_month in d.items() if month in d[cur_season]][0].capitalize()
    return f"Current season is: {cur_season}"


print(season(input('Type the current month: ')))

import numpy as np
years = np.arange(1900, 2020+1, 1)

def leap_year(x, function):
    return function(x)

def leap_year_400(num):
    return num%400 == 0

def leap_year_100(num):
    return num%100 != 0

def leap_year_4(num):
    return num%4 == 0

def leap_year_list():
    leap_years = []
    for year in years:
        if leap_year(year, leap_year_400) or (leap_year(year, leap_year_100) and leap_year(year, leap_year_4)):
            leap_years.append(year)
    return leap_years

while True:
    try: 
        month = int(input('Enter month number: '))
        if month > 12:
            raise ValueError
        elif month <= 0:
            raise ValueError
    except ValueError:
        print('Please, enter number from 1 to 12!')
        continue
    else:
        break

while True:
    try:
        year = int(input('Enter year: '))
        if year < 1900:
            raise ValueError
        elif year > 2020:
            raise ValueError
    except ValueError:
        print('Enter year from 1900 to 2020!')
        continue
    else:
        break

def days_in_month(month, year, leap_year_list):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        if year in leap_year_list:
            return 29
        return 28
    return 30

print('Days in this month: ', days_in_month(month, year, leap_year_list()))
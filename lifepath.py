# life path number assigns a number to the month you were born in and then adds the numbers from the rest
# and reduces them down to a single digit (unless it's 11 or 22)
# MONTH may/5 = 5

# DAY = 29
# 2 + 9 = 11 (no further reduction)

# YEAR = 1981
# = 1 + 9 + 8 + 1 = 19
# = 1 + 9 = 10
# = 1 + 0 = 1

# 5 + 11 + 1 = 17
# 17 = 1 + 7 = 8

# my life path number = 8

import numpy as np
from functools import reduce


monthsum = []
daysum = []
yearsum = []
prefinal = []


# ask the user for their month, day, and year of birth
month = input("Enter the number of the month of your birth \n")
day = input("Enter the number for the day of your birth \n")
year = input("Enter the full year of your birth \n")
#print("So your full birth date is " + month + "/" + day + "/" + year + "?")


# take user's input for month and reduce down to single digit unless it's 11 and print the result
# WORKING
if month == "11":
    print("11 is correct here.")
    # append this to prefinal
else:
    monthsum = sum(int(digit) for digit in str(month))
    print("result of month is " + str(monthsum)
    # append this to prefinal


# reduce the user's input for the day of their birth down to a single digit unless it's 11 or 22 and print the result
# WAS WORKING
if day == "11" or day == "22":
    print("result of day is " + day + ".")
    # append this to prefinal
else:
    daysum = sum(int(digit) for digit in str(day))
    if daysum == "11":
        print("you got 11 for daysum.")
    # append this to prefinal

# reduce the user's input for the year of their birth down to a single digit unless it's 11 or 22 and print
# first part WORKING
yearsum = sum(int(digit) for digit in str(year))

if str(yearsum) == "11" or str(yearsum) == "22": # this is working
    print("Wow " + str(yearsum) + "," + " aren't you special.") # this is working
else:
    if str(yearsum) < "10":
        print("year reduced a 2nd time")

print(yearsum)





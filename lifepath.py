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
final = []


# ask the user for their month, day, and year of birth
month = int(input("Enter the number of the month of your birth \n"))
day = int(input("Enter the number for the day of your birth \n"))
year = int(input("Enter the full year of your birth \n"))
# ignore this for now print("So your full birth date is " + str(month) + "/" + str(day) + "/" + str(year) + "?")


# take user's input for month and reduce down to single digit unless it's 11 and print the result
if month == 11:
    print("11 is correct here.")
    prefinal.append(month)
else:
    monthsum = sum(int(digit) for digit in str(month))
    print("result of month is " + str(monthsum))
    prefinal.append(month)


# reduce the user's input for the day of their birth down to a single digit unless it's 11 or 22 and print the result
if day == 11 or day == 22:
    print("result of day is " + str(day) + ".")
    prefinal.append(day)
else:
    daysum = sum(int(digit) for digit in str(day))
    print("reduced day result is " + str(daysum))
    prefinal.append(daysum)


# reduce the user's input for the year of their birth until it's a single digit unless it's 11 or 22
yearsum = sum(int(digit) for digit in str(year))

if yearsum == 11 or yearsum == 22: # try 1975 = 22
    print("your year reduced once down to magic number " + str(yearsum))
    prefinal.append(yearsum)
elif yearsum > 10:
    yearsum2 = sum(int(digit) for digit in str(yearsum))
    if yearsum2 == 11 or yearsum2 == 22:
        print("result of day is " + str(yearsum2) + ".")
        prefinal.append(yearsum2)
    else:
        yearsum3 = sum(int(digit) for digit in str(yearsum2))
        print("reduced day result is " + str(yearsum3))
        prefinal.append(yearsum3)
else:
        print("your year number is " + yearsum)
        prefinal.append(yearsum)

# print the list of numbers to be added
print("the list of numbers to be added together is " + str(prefinal))

# now add each number together
final = sum(prefinal)
print("before reducing your numbers add up to " + str(final))

# now see if that final number equals to 11 or 22 and to proceed as we did with year number
if final == 11 or final == 22:
    print("your life path number is special number" + str(final))
elif final > 10:
    final2 = sum(int(digit) for digit in str(final))
    if final2 == 11 or final2 == 22:
        print("your life path number reduces once down to special number " + str(final2) + ".")
    else:
        final3 = sum(int(digit) for digit in str(final2))
        print("your life path number reduces down once to " + str(final3))
else:
        print("your life path number doesn't reduce down and it is " + final)





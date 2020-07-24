# the birthday is derived by reducing the day of birth to a single digit or master number (11, 22)

import pytest

birth = int(input("Enter the number of the month of your birth \n"))

def reducebirth():
    if birth == 11 or birth == 22:
        print("your birthday number is master number" + str(birth))
    elif birth > 10:
        birth2 = sum(int(digit) for digit in str(birth))
        if birth2 == 11 or birth2 == 22:
            print("your life path number reduces once down to special number " + str(birth2) + ".")
        else:
            birth3 = sum(int(digit) for digit in str(birth2))
            print("your life path number reduces down once to " + str(birth3))
    else:
        print("your life path number doesn't reduce down and it is " + str(birth))




reducebirth()

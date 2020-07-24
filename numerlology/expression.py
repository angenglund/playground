# the expression is derived by finding the sum of the  number of values of all the letters in each name, reducing this
# sum to a single digit or master number, then adding the sums of all the names together and reducing that total to a
# single digit or master number (11, 22)



def special_sum(number):
    # This is a hack, because if it's a string we can split up the digits
    number_as_string = str(number)

    # If we only have a single digit, we don't need to continue, we've hit gold
    if len(number_as_string) == 1 or len(number_as_string) == 11 or len(number_as_string) == 22:
        return number_as_string

    # See above note about the hack, 55 -> "55" -> ["5", "5"]
    list_of_characters = list(number_as_string)

    # Because we need to sum the numbers, we need it to be a list of numbers ["5", "5"] -> [5, 5]
    list_of_numbers = map(int, list_of_characters)

    # Now we need to take our list of numbers and add them together, aggregating a total
    sum_of_numbers = sum(list_of_numbers)

    # Finally, restart the process with the new sum
    return special_sum(sum_of_numbers)


# the thing that holds your expression number
exnum = []

# greeting + ask a yes or no
print("Hello. I'm here to give you your numerology report. Would you like to know your Expression number?\n")
helloask = input("Yes / No\n")

# if no to expression number, goodbye and quit
# if helloask == "no":
if helloask in ["no"]:
    quit("wow ok sorry to bother you then bye")
# if anser yes to expression number, get birth name
else:
    birthname = input("ok cool i guess. what is the full name on your birth cirtificate?\n")
    # confirm name is correct
    print("a'ight so your full name is " + birthname + "? you sure about that?")
    nameconfirm = input("Yes / No\n")
# if name is wrong
if nameconfirm in ["no"]:
    birthname = input("ok go ahead and tell me again. speak up this time!\n")
    print("ok one more time: is " + birthname + " on your birth certificate?\n")
    nameconfirm = input("Yes / No\n")
# if name is wrong AGAIN
if nameconfirm in ["no"]:
    quit("i'm done with you. come back later when you can type straight.")

else:  # if name is confirmed
    print("ok just let me calculate that for you. hmm so add this, carry the blue, rotate that...\n")
    print("wow so i guess your Expression number is ")

# the chart
chart1 = ['a', 'j', 's']
chart2 = ['b', 'k', 't']
chart3 = ['c', 'l', 'u']
chart4 = ['d', 'm', 'v']
chart5 = ['e', 'n', 'w']
chart6 = ['f', 'o', 'x']
chart7 = ['g', 'p', 'y']
chart8 = ['h', 'q', 'z']
chart9 = ['i', 'r']

# converting numbers to letter values
for num in chart1:
    if num in birthname:
        exnum.append(1)
for num in chart2:
    if num in birthname:
        exnum.append(2)
for num in chart3:
    if num in birthname:
        exnum.append(3)
for num in chart4:
    if num in birthname:
        exnum.append(4)
for num in chart5:
    if num in birthname:
        exnum.append(5)
for num in chart6:
    if num in birthname:
        exnum.append(6)
for num in chart7:
    if num in birthname:
        exnum.append(7)
for num in chart8:
    if num in birthname:
        exnum.append(8)
for num in chart9:
    if num in birthname:
        exnum.append(9)

print(special_sum(sum(exnum)))
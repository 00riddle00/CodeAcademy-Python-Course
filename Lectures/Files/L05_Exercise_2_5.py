# E.2.5.
# • Create a program which would:
#     • Ask a user to enter a year.
#     • Print "Leap year", if that's the case.
#     • Else, print "Not a leap year".

year = int(input("Enter a year > "))

if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')

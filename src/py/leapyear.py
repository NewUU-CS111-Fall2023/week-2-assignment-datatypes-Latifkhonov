def checkleap(year):
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        print("Given year is a leap ")
    else:
        print("Given year is not a leap")

year = int(input("Enter a year: "))
checkleap(year)
year = int(input("enter your year:"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("it is leap year")
else:
    print("it is not leap year")

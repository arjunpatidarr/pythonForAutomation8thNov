#check leap year
#if (year%4==0 and year%100!=0) or (year%400==0):

year = 2001

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("given year is a leap year")
        else:
            print("Not a leap year")
    else:
        print("Is a leap year")
else:
    print("Not a leap year")
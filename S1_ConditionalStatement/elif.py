#validate number is positive, negative and zero

num = 3
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
elif num==0:
    print("number is zero")


#Leap Year Checker
# It is divisible by 4.
# However, if it is divisible by 100, it is NOT a leap year, UNLESS...
# It is also divisible by 400.

year = 2001
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Given year is a leap year")
else:
    print("given year is not a leap year")

#Grading System: Write a program that takes a student's score (0-100) as input and prints their corresponding grade:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
score = 60
if(score>=90 and score<=100):
    print("Grade is A")
elif(score>=80 and score<=89):
    print("Grade is B")
elif(score>=70 and score<=79):
    print("Grade is C")
elif(score>=60 and score<=69):
    print("Grade is D")
else:
    print("Grade is F")
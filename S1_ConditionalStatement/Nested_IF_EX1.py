#find the largest number

num1 = 10
num2 = 20
num3 = 30

if(num1>num2):
    print("num1 is greater than num 2")
elif (num1>num3):
    print("num1 is greater than num 3")
else:
    print("num1 is less than 2 and 3")

if(num2>num3):
    print("num2 is greater than num 3")
elif (num2>num1):
    print("num2 is greater than num 1")
else:
    print("num2 is less than 3 and 1")

if(num3>num1):
    print("num3 is greater than num 1")
elif(num3>num2):
    print("num3 is greater than num 2")
else:
    print("num3 is less than 1 and 2")

#correct way


if(num1>num2):
    if(num1>num3):
        print("num1 is largest")
    else:
        print("num 3 is largest")
else:
    if(num2>num3):
        print("num2 is largest")
    else:
        print("num3 is largest")
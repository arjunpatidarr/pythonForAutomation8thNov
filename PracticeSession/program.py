

#num =2 start and divide with itself 2,3,5,7,11,13,17,19
num = int(input("enter a number: "))

if num<=1:
    print("given number is not prime")
elif num==2:
    print("given number is prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("given number is not prime")
            break
    else:
        print("given number is prime")



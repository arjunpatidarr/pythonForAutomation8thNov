
num1 = 30
num2 =0
try:
    divide = num1 / num2
    print(divide)
except ZeroDivisionError:
    print("Exception block")


print("-------------------EX-2-----------------------")

num1 = int(input("Enter a First number:" ))
try:
   num2 = int(input("Enter a Second number: "))
   divide = num1/num2
   print(divide)
except ValueError:
    print("value error because int can't divide by string or char")
except ZeroDivisionError:
    print("can't divide by zero try with different integer")

print("execution is completed")
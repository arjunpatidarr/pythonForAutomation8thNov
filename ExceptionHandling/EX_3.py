num1=int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))
num2 = "abc"
try:
    Result = num1/num2
    print(Result)
except ZeroDivisionError:
    print("Division by zero")
except TypeError:
    print("Type error")
except Exception as e:
     print(e)
     print("handling generic exception")

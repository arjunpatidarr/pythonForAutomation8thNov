
num1 = int(input("Enter the first number: "))
num2 = input("Enter the second number: ")

try:
    result = num1/num2
    print(result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("divide by zero is not possible")
# except Exception as e:
#     print(e)
#     print("this is generic exception handler")
except TypeError:
    print("Unsupported operation")

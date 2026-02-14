a =10
#b = 0
b = "abc"

try:
    c = a/b
    print(c)
except ValueError:
     print("Value error")
except TypeError:
    print("Type error")
except:
    print("Unexpected error")
finally:
    print("cleanup activity")

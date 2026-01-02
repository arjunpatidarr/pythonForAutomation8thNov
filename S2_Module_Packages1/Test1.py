def fun():
    print("Funtion from Test 1 module and Package1")

def add(a,b):
    print("Addition of given num is:", a+b, "From PAckage one")

num1 = 10

class A:

    num2 = 30
    def __init__(self):
        print("User defined Constructor from Test 1 module and from Package 1")

    def m1(self,a,b,c):
        print(a+b+c)

    def m2(self):
        print("Running method-m2 from Test1 Module1")

    @staticmethod
    def static_meth():
        print("Static method from Test1 Module1")
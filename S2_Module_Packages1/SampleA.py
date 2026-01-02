def  fun1():
    print("fun1 from Sample A Module")

def  add(a,b):
    return a+b

num1 = 90
num2 = 100

class  Demo:
    a =20
    b=10
    def __init__(self):
        print("Demo Constructor")

    def m1(self):
        print("method from m1")

    def m2(self,a,b,c):
        print(a+b+c)

    @staticmethod
    def methStatic():
        print("static method")

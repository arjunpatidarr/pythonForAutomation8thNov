
def fn1():
    print("fn1 from class A")

def fn2():
    print("fn2 from class A")


num1 = 20
num2 = 30

class X:

    def meth(self,a,b):
        c = a+b
        print("method from class X", c)

    def meth2(self):
        print("method from class X")

    def xyz(self):
        print("method from class X")

class Y(X):

    def meth(self, a, b):
        c = a - b
        print("method from class Y", c)

    def meth2(self):
        super().meth2()
        print("method from class Y")

obj = Y()
obj.meth(1,2)
obj.meth2()
#obj.xyz()
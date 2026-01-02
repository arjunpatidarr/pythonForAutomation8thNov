
a = 2
b =3


def fn():
    a =10
    b=90
    print("Function", a+b)

class A:

    a = 5
    b=9

    def __init__(self,a, b):
        self.x = a
        self.y = b
        print(self.x,self.y)

    def m1(self):
        c = self.a+self.b
        print(c)

    def add(self, a, b):
        print(a+b)
        print(globals()["a"]+globals()["b"])

print(a,b)
d = A(2,2)
d.add(3,5)
fn()
d.m1()


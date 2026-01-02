class A:

    num1 = 1
    def m1(self):
        print("A")

    def m2(self):
        print("A")

    @staticmethod
    def StatA():
        print("Static Method from Class A")

class B(A):
    num2 = 10
    def m1(self):
        print("B")

    @staticmethod
    def StatB():
        print("Static Method from Class B")

class C(B):
    num2 = 20
    def m2(self):
        print("C")

    @staticmethod
    def StatB():
        print("Static Method from Class C")

obj = C()
obj.m1()
obj.m2()
print(obj.num1)
print(obj.num2)
C.StatB()
B.StatB()
C.StatA()


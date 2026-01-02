class  A:

    def  Class1(self):
        print("Class A method")

    def class2(self):
        print("Class B method")

class B:

    def class3(self):
        print("Class C method")

    def class4(self):
        print("Class D method")

class C(A,B):

    def  method123(selfself):
        print("Method 123")

obj = C()
obj.method123()
obj.Class1()
obj.class3()


class  X:

    def m1(self):
        print("m1")

class Y(X):
    super().m1
    def m1(self):
        print("m2")

obj = Y()
obj.m1()
obj2 = X()
obj2.m1()
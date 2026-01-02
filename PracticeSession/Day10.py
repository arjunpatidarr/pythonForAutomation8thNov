
#inheritance

#single level - perform b/w 2 classes

class A:
    num1 =10  #class variable
    def m1(self ):
        print("M1 from A")

class B(A):

    def m2(self):
        print("M2 from B")
        print(self.num1)

obj = B()
obj.m1()
obj.m2()
print(obj.num1)

print("-------------------------")
# multi level in heritance
#perform betwwen 3 classes or more

class X:
    def m1(self):
        print("M1 from X")

class Y(X):
    def m2(self):
        print("M2 from Y")

    @staticmethod
    def m5():
        print("Static method from Y class")

class Z(Y):

    def m3(self):
        print("M3 from z")

obj1 = Z()
obj1.m1()
obj1.m2()
obj1.m3()
obj1.m5()
Z.m5()
Y.m5()


print("----------------------------")
#Hiearchical inheritance one super class aquire by multiple sub classes

class Sample1:

    def __init__(self,a,b):
        c = a+b
        print("User defined constructor",c)

    def x(self):
        print("x method from Sample1")

class Sample2(Sample1):

    def y(self):
        print("y method from Sample2")

class Sample3(Sample1):

    def z(self):
        print("z method from Sample3")


obj2 = Sample2(4,5)
obj2.x()
obj2.y()
obj3 = Sample3(8,9)
obj3.z()

print("_--------------------------_____________-")
#one sub class aquiring propertied of 2 super class is called multiple level inheritance

class super1():
    def m1(self):
        print("M1 from super1")

class super2:
    def m2(self):
        print("M2 from super2")

class super3:
    def m4(self):
        print("M4 from super3")

class subClass(super1,super2,super3):
     def m3(self):
            print("M3 from subClass")

obj = subClass()
obj.m1()
obj.m2()
obj.m3()
obj.m4()


print("----------------------extra-------------")

class Demo():
    def m1(self):
        print("M1 from Demo")

obj = Demo()
obj.m1()
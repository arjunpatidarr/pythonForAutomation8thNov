
class parent:
    name = "amol"

class child(parent):
    name = "Amol"

    def studentName(self):
        print("Student Name from SUb Class :", self.name)
        print("Student Name from Super class :", super().name)
        num=super().name
        print(num)


obj = child()
obj.studentName()

print("--------------------")

class A:
    num2 = 10

    def __init__(self,a,b):
        c = a+b
        print("user defined constructor",c)

    def m1(self):
        print("method m1 from class A")

class B(A):
    num2 = 11
    def m2(self):
        print("method m2 from class B")
    def m1(self):
        print("method m1 from class B")


obj = B(2,3)
obj.m1()
print(obj.num2+obj.num2)

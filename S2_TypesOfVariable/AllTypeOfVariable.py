
num1 = 10  #global

class Demo:

    num2 = 30  #class

    def __init__(self, a):
        self.num3 = a  #class

    def  m1(self,num4):
        num5 = 60
        print(num1)
        print(self.num2)
        print(self.num3)
        print(num4)
        print(num5)

d = Demo(4)
d.m1(9)

class Demo4:

    def __init__(self,num):
        self.num1=num

    def SqaureOfNum(self):
        print(self.num1*self.num1)

    def CubeOfNum(self):
        print(self.num1**3)


d1 = Demo4(2)
d1.SqaureOfNum()
d1.CubeOfNum()

print("--------------")

d1 = Demo4(4)
d1.SqaureOfNum()
d1.CubeOfNum()

print("--------------")

d1 = Demo4(5)
d1.SqaureOfNum()
d1.CubeOfNum()
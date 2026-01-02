
class  Demo6:

    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print(self.num1+self.num2)

    def sub(self):
        print(self.num1-self.num2)

    def mul(self):
        print(self.num1*self.num2)

    def div(self):
        print(self.num1/self.num2)

obj = Demo6(10,2)
obj.add()
obj.sub()
obj.mul()
obj.div()




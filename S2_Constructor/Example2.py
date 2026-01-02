class  Demo:

    def __init__(self,num):
        self.num1 = num
        print("S2_Constructor")

    def  method(self):
         print(self.num1*self.num1)
         print("instance Method/ Non static method")
         print("Square")

    @staticmethod
    def  method1():
        print("Static Method")

Obj = Demo(2)
Demo.method1()
Obj.method()



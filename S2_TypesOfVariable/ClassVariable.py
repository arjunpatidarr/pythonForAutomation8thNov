
class MyClass:

    a = 10

    def __init__(self,b):
        self.b = b
        print("MyClass S2_Constructor", b)

    def m1(self):
        print("MyClass Method")

    def add(self):
        print("Addition of given is :", self.a+self.b)


    def Square(self):
        c = self.a*self.b
        return  c


d = MyClass(1)
d.add()
result = d.Square()
print(result)
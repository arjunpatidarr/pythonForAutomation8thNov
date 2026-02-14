

class Student:

    var = 10

    def __init__(self,name):
        ls = 20
        self.name = name
        print("constructor",name)

    def mth(self, sur):
        self.sur = sur
        print(self.name)
        print("m1")
        print(sur)

    def m1(self):
       print("Method 1")


obj = Student("Arjun")
obj.mth("patidar")
obj.m1()
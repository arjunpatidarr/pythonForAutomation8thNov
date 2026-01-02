
class GrandParent:

    def method1(self):
        print("method1 from class GrandParent")

    def car(self):
        print("car from class GrandParent")

class Parent(GrandParent):

    def method1(self):
        print("method1 from class Parent")

class Son(Parent):
    def method1(self):
        print("method1 from Son")

obj = Son()
obj.method1()
obj1 = Parent()
obj1.method1()
obj1.car()
obj.car()
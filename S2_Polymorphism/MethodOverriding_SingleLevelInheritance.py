class A:

    def method1(self):
        print("method1 from class A")

    def method2(self):
        print("method2 from class A")

class B(A):
    def method1(self):
        print("method1 from class B")

obj = B()
obj.method1()
obj.method2()

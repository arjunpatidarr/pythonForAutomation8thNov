
num = 10

def  fn():
     print("first function")
     print(num)



class  Demo:

    def __init__(self):
        print("S2_Constructor")
        print(num)

    def m1(self,a):
        print("Method inside Class")
        print(num+a)

print("Call Global Variable:", num)
d = Demo()
d.m1(3)

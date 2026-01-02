# num1 = 10
# num2 = 20

print("--------Local Variable in funtions----------")

def meth(num1, num2):
        print("multiplication of given num is :",num1*num2)

def meth2():
        a = 10
        print("Method2")

meth2()
meth(2,2)



print("-------Local Variable in Methods----------")


class Sample:

    def  add(self):
        num1 = 10
        num2 = 20
        print("Addition :",num1+num2)

    def sub(self,Num1, Num2):
        print("Subtraction :",Num1-Num2)

d = Sample()
d.add()
d.sub(10,20)


print("--------Local Variable in S2_Constructor--------")

class Sample1:


   def  __init__(self,c):
        a = 10
        b=20
        print("S2_Constructor Variable", c)


d=Sample1(2)

    
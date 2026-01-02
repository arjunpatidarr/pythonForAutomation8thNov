# Struture Oriented -
# Object oriented  - need a class and object to run any code


def  fn():
    print("fn")

fn()


#class

def cew():
    print("New Function")

cew()
a =8
b=90
class A:
     num1 = 10
     num2 = 20

     def m1(self):
         c = a+b
         d = 90
         num3 = self.num1+self.num2
         print("M1")


#methods

# 1)Static/classs method
# 2)nom static/instance method


class X:


    def  mth(self):
        c=30+50
        print(c)



    def add(self,a,b):
         print(a+b)


    def square(self,x):
        return x*x

s1 = X()
s1.mth()
s1.add(4,5)
w = s1.square(9)
print(w)






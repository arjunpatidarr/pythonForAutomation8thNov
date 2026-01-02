
#method Overloading

class A:

   def  add(self, a=0,b=0,c=0,d=0):
        print(a+b+c+d)

   # def add(self,a,b):
   #    print(a+b)
   #
   # def add(self, a,b,c):
   #    print(a+b+c)
   #
   # def add(self,a,b,c,d):
   #     print(a+b+c+d)



obj = A()
obj.add(1)
obj.add(1,2)
obj.add(1,2,3,4)

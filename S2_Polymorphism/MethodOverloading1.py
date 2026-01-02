
class  Student:
    # def add(self, a, b):
    #     print(a+b)
    #
    # def add(self,a,b,c):
    #     print(a+b+c)
    #
    # def add(self, a,b,c,d):
    #     print(a+b+c+d)

    def  add(self, a=0,b=0,c=0,d=0):
        print(a+b+c+d)

d = Student()
d.add()
d.add(5,10)
d.add(2,3,4)
d.add(1,2,3,4)
d.add(0,0,1,2)

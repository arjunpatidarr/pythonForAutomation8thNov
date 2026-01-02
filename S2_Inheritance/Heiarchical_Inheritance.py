
class Father:

    def  property(self):
        print("Having and house and villa")

    def  car(self):
        print("Having Car: Swift")

class Son1(Father):

    def mobile(self ):
        print("Having Mobile")



class Son2(Father):

    def Laptop(self):
        print("Having Laptop")

Obj = Son1()
d = Son2()
Obj.property()
d.mobile()

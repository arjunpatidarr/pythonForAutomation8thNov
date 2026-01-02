class  Father:
    
    def money(self):
        print("Money")
        
    def  car(self):
        print("Car")
        
    def  House(self):
        print("House")
        
class Son(Father):
    
    def mobile(self):
        print("Mobile")

d = Father()
d.money()
Obj = Son()
Obj.mobile()
Obj.money()
Obj.House()
Obj.House()
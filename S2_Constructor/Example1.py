class  Demo4:

    def __init__(self):
        print("User defined constructor")


    def  factorial(self, num):
        fact = 1
        for i in range(1 , num+1, 1):
            fact = fact * i
        print(fact)

s1 = Demo4()   #object creation -> consructor will be call >> intialise object
s1.factorial(10)    #copy all members of class into object
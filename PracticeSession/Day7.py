
#construtor

# class A:
#
#   x = 90
#   y=80
#
#   def __init__(self, a,b):
#     print(a+b)
#     z = self.x+self.y
#     #print("user defined constructor", z)
#
#
#
#
#s1 = A(2,3)

# why we are not using self keyword in static method? because it does not refer to any object And it does not use instance data

num1 = 10
num2 = 30

class  B:

    # def __init__(self):
    #     num3 = num1+num2
    #     print(num3)

    def  __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        print(num1*num2)

B(2,4)



# single - 2clasess
# multi level - 3 or more classes
# hiearchical - parent - 2 sub class(multiple child)
# multiple inheritance - 2 super clasees - aquire property of one sub(single child)
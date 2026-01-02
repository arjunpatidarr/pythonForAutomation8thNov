
class Demo6:


    def __init__(self):
        print("S2_Constructor is running")


    @staticmethod
    def  add(num1, num2):
        print("addition of given number is :" ,num1 + num2)

    @staticmethod
    def  mul(num1, num2):
        print("Multiplication of given number is :", num1 * num2)


Demo6.mul(10,20)
Demo6.add(2,5)

class Demo2:

    def substraction(self, num1, num2):
        print("Substraction:" ,num1 - num2)


    def test(self):
        print("testing non static or instance method")

    @staticmethod
    def  square():
        print("Run Static Method")

    @staticmethod
    def  testing():
        print("testing static method")


s1 = Demo2()
s1.substraction(6,2)
s1.substraction(10,34)
s1.substraction(12,45)

Demo2.square()
Demo2.testing()
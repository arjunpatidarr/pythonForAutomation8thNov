class  Demo:
    a =10
    b= 20
    print(a+b)
#method without parameter
    def  m1(self):
        print("first method")

    def  m2(self):
        print("second method")

#method with paramter

    def addition(self, num1, num2):
        print("addition of given number is:-", num1+num2)

    def sqaureOfGivenNum(self, num):
       print("Square of given number is", num*num)

s1 = Demo()
s1.m1()
s1.m2()
s1.addition(1,2)
s1.sqaureOfGivenNum(20)

print("------------------")
s2 =Demo()
s2.sqaureOfGivenNum(100)

from S2_Module_Packages1  import Test1

Test1.fun()
Test1.add(3,4)
obj = Test1.A()
obj.m2()
obj.m1(1,3,6)
Test1.A.static_meth()
print(Test1.num1+Test1.A.num2, "Calling variable from Package 1")
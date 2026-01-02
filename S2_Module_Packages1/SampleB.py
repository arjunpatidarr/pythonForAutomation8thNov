# import SampleA
#
# result = SampleA.num1 + SampleA.num2
# print(result)
#
# result1 = SampleA.add(5,4)
# print(result1)
#
# SampleA.fun1()
#
# SampleA.Demo.methStatic()
# A = SampleA.Demo()
# A.m2(4,5,6)
# SampleA.Demo()


# from SampleA import Demo, add, fun1
#
# S = Demo()
# S.m2(1,3,7)
# Demo.methStatic()
# store = add(4,5)
# print(store)
# fun1()

from SampleA import *


S = Demo()
S.m2(1,3,7)
Demo.methStatic()
store = add(4,5)
print(store)
fun1()
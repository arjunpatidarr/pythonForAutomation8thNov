
#approach 1 to call one module data to another

import FileA

c = FileA.num1+FileA.num2
print(c)

FileA.add(3,4)
Output = FileA.square(2)
print(Output)

d = FileA.A()
d.m1()
Out = d.mult(4,4)
print(Out)


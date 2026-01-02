#approach 2.1 to call one module data to another

from FileA import A, num1,num2, add,square

print(num1)
print(num2)
add(2,5)
output = square(9)
print(output)

d = A()
x = d.mult(5,9)
print(x)

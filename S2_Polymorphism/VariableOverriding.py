
#variableOverriding/variable reinitialisation

class A:
    name = "AMol"

class B(A):
    name = "amol"

obj = B()
print(obj.name)
class Employee:
    company = "Google"          # Class Variable (Shared)

    def __init__(self, name):
        self.name = name
        print(name)# Instance Variable (Unique)

# Creating two objects
e1 = Employee("Alice")
e2 = Employee("Bob")
print("------------")
# If we change a Class Variable:
Employee.company = "Meta"
print(e1.company)  # Output: Meta
print(e2.company)  # Output: Meta (Everyone sees the change)

# If we change an Instance Variable:
e1.name = "Alicia"
print(e1.name)     # Output: Alicia
print(e2.name)     # Output: Bob (Only e1 changed)

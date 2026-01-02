
class Demo5:

    def __init__(self,empName, empID, empSalary, empDesignation):
        self.empName = empName
        self.empID = empID
        self.empSalary = empSalary
        self.empDesignation = empDesignation

    def method1(self):
        print("empName", self.empName)
        print("empID", self.empID)
        print("empSalary", self.empSalary)
        print("empDesignation", self.empDesignation)


emp1 = Demo5("Arjun", 12345, 100000, "AUTOMATION TESTER")
emp2 = Demo5("bhupesh", 92345, 800000, "Developer")
emp3 = Demo5("Rupesh", "34567", 20000, "Media")

emp1.method1()
print("-----------------")
emp2.method1()
print("-----------")
emp3.method1()
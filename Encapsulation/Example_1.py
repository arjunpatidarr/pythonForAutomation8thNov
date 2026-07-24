class Person:

    def __init__(self,name,age, school):
        self.__name = name
        self.__age = age
        self.school = school

    def display(self):
        print(self.__name)
        print(self.__age)
        print(self.school)

    def __dataa(self):
        print("private method")

    def car(self):
        print("Car Method")
        self.__dataa()

obj = Person("Ram",18, "Maa Bharti")
obj.display()
obj.school ="Allen"
obj.name = ""
obj.display()
obj.car()

class Person:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def display(self):
        print(self.__name)
        print(self.__age)

    def __dataa(self):
        print("private methoda")


obj = Person("Ram",18)
obj.display()
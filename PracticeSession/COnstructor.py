class A:

  # def __init__(self):

   def __init__(self, name, age, clg="MIT"):
        self.name = name
        self.age = age
        self.clg = clg
        print(self.name, self.age, self.clg)

x = A("John", 18, "symbiosis")
y = A("Lakhan", 19)
z = A("Smith", 20)

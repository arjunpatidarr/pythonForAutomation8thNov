
class A:

    def student1(self):
        print("Student1 from Class A")

    def student2(self):
        print("Student2 from Class A")

class B(A):

    def student1(self):
        super().student1()
        print("Student1 from Class B")

obj = B()
obj.student1()
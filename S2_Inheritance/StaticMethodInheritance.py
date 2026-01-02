class  A:

    @staticmethod
    def School():
        print("school method of class School")

    @staticmethod
    def Room():
        print("Room method of Class A")

class B(A):
    @staticmethod
    def  School():
        print("School method of class B")

B.School()
B.School()
B.Room()
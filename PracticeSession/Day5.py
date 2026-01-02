
class A:

    def m1(self ):
        print("method m1 from class A")

    def __init__(self):
        print("Constructorfrom class A")

    @staticmethod
    def stat():
        print("Static method from class A")

class B(A):

    def m2(self ):
        print("method m2 from class B")

    def __init__(self):
        print("Constructorfrom class B")

d = B()
d.m1()
d.m2()
B.stat()


print("-----------")

ls = ["abc",1,2,3,4,5,90]
st ={"abc",45,32,"wer",23}
st_ls = list(st)
print(st_ls)
print(ls)

ls_1 = set(st_ls)
print(ls_1)
print("--------------")

x = [12,34,56,43,56,87,90,2]
x.sort()
print(x)

z = {"wer", "abc", "wer", "ghi", "ZAR"}
q = sorted(z)
print(q)
si = "abcdefg"
print(len(si))
print(len(ls))

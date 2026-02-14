#
# inp = input("please enter a String:")
# rev = inp[::-1]
#
# if inp ==rev:
#     print("Given String is Pallindrome")
# else:
#     print("Given String is not Pallindrome")


#or

inp = input("please enter a Name:")
rev = ""

for i in  inp:
    rev = i+rev
if rev ==inp:
    print("Given String is Pallindrome")
else:
    print("Given String is not Pallindrome")
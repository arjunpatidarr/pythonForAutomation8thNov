# ls = [12,1,2,1,2,1,34,3,2,324,33,22,2,2,3,3]
# ls = sorted(ls)
# print(ls)
# st = set(ls)
# print(st)

print("Write a function to remove duplicates from a list while maintaining the original order.")

def fn():
    user_Input = input("enter a number to store in a list:")
    ls = user_Input.split()
    st = set(ls)
    final_output =list(st)
    print(final_output)

#fn()

print("below with correct way----------------")

# ls = [ 12,3,4,5,6,2,2,24,5]
# d = dict.fromkeys(ls)
# print(d)

def fn():
    user_Input = input("enter a number to store in a list:")
    final_output = (dict.fromkeys(user_Input))
    print(final_output)
fn()





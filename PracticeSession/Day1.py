
ls = []
ls1 = ["abc", 1,2,3,4,"e"]
ls2 = [1,2,3,4,5,1,2,3]

print(ls2)
print(len(ls))

# add element in the list


ls1.append("xyz")
print(ls1)

ls1.insert(4, 40.5)
print(ls1)

ls1.extend([10,45,"wdc"])
print(ls1)

# remove element from the list

ls1.pop()
print(ls1)

ls1.pop(4)
print(ls1)

ls1.remove(1)
print(ls1)


ls1[0] = "cba"
print(ls1)

print(ls1[1])


# copy list

ls2 = ls1.copy()
print(ls2)

#print data

for i in ls2:
    print(i)
print("--------------------")
print(len(ls2))
for i in range(0, len(ls2)):
    print(ls2[i])

print("------------")
for i in range(len(ls2)-1, -1, -1):
    print(ls2[i])


#sorting operation
ls3=[34,56,2,1,34,5,6,7,54]
ls3.sort()
print(ls3)

ls3.reverse()
print(ls3)


ls4=["jhg","asd", "awe", "rty", "aad"]
ls4.sort()
print(ls4)

#clear the list

ls3.clear()
print(ls3)

#delete the list
del ls3


s2=[1,5,2,6,7,8,0,2,8,2,1]

print(s2.index(5))   #return index of element ->1st occurrence
print(s2.count(2))
s1 = ["sdx", "dfc", "awe",4,5,6,7,23,4]
print(s1+s2)



#convert list into set
print("----------")
print(s2)
s5 = set(s2)
print(s5)

my_list = [1, 1, 2, 3, 2, 4]
my_list = list(set(my_list))
print(my_list)
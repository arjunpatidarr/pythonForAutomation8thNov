
ls = [12,34,6,45, "arjun", "patidar"]
print(len(ls))
print(ls)
print(type(ls))

#add data at last
ls.append(123)
print(ls)

ls.insert (0,"julmi")
print(ls)

ls.extend([23, "April", 1998])
print(ls)

#delect data from list

ls.pop()
print(ls)

ls.pop(0)
print(ls)

ls.remove(6)
print(ls)

print(ls[0]) #get data from list by passing index number

ls[5] = 321  #reinstallisation of index 5
print(ls)

ls1 = ls.copy()
print(ls1)

for i in ls:
    print(i)

for i in range(0,len(ls)):
    print(ls[i])

for i in range(len(ls)-1, 0-1, -1):
     print(ls[i])

ls1.reverse()
print(ls1)

#sorting data type

list = [1,23,4,56,45,321]
list.sort()
print(list)

list.reverse()
print(list)

list.insert(3, 321)
list.insert(4,1)
print(list)
print(list.count(321))

list.clear()
print(list)

list = ls.copy()
print(list)

del list
print(list)




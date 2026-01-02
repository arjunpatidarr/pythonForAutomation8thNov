#set is used to store unique value

st = {12,23,12,23,24}
print(st)

st1 = {12,34,56,12,23,"Arjun", "patidar", "set"}
print(st1)
print(len(st1))
print(type(st1))
print(st1)

st2 = {1,2,3,4,5,6,7,8,9,10,10,10}
print(len(st2))

st2.add("Arjun")
print(st2)
st2.add("patidar")
print(st2)
st2.update({"julmi", "kota", 326519})
print(st2)

#to remove specific data from set
st2.remove(326519)
print(st2)
# if you plass invalid iinput while remove data it will throught error message

st2.discard("326519")
print(st2)
#it does not display any error messgae in console if we pass an incorrect input or data to remove

#to remove random elelemnt from the set

st2.pop()
print(st2)
st2.pop()
print(st2)

finalSet = st2.copy()
print(finalSet)

#sorting of set

et = {1,2,34,12,67,89,98,23, 10.4, 32.5}
print(et)

et1 = sorted(et)
print(et1)

#sorting will be done only when we have homogenous data
x = {1,2,3,4,12,34,"Arjun","Patidar"}
#y = sorted(x)
#print(y)


#convert set into list

z = list(x)
print(z)

#convert list into set
q = set(z)
print(q)

#clear set from object

po = {1,23,34,56,76,5,4,3,2.1,"Arjun", "patidar"}
po.clear()
print(po)

#del set using delete funtion
del po
#print(po)
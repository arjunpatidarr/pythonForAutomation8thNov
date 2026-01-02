dict1 = {"Arjun" : 90, "Ravi":90, "Shubham" :80}
print(dict1)

# to reinstallisation of any key value?

dict1["Arjun"] = 96
print(dict1)
print(len(dict1))
print(dict1["Ravi"])

dict1["patidar"] = 67.7
print(dict1)

dict1["kota"]= 326519
print(dict1)

#delete and remove specific key value
dict1.pop("Ravi")
print(dict1)

#delete recent data or last dict data
dict1.popitem()
print(dict1)

#in dict need to check specific key?
print("kota" in dict1)
obj = "kota" in dict1
print(obj)
if obj == False:
   print("Given data is not available in dictionary")

#Get all keys from dictionary

allKeys = dict1.keys()
for key in allKeys:
    print(key)

#get all values from dictionary

allValue = dict1.values()
for values in allValue:
    print(values)

#get all key and value pair from dict

allitems = dict1.items()
for Key, Value in allitems:
    print(Key,":",Value)


dict = {"Lakhan":25, 123:"AMol", 'abc':45.06, "AMol":345, 123:456, 'abc':567}

print(dict)
print(dict)

#to get specific key value?

print(dict.get("Lakhan"))
print(dict["Lakhan"])


#add any new K-V

dict["Arvind"] = 90
print(dict)

dict["Monu"] = 91
print(dict)

#Update or modify

dict["Lakhan"] = 56
print(dict)

dict.update({"Lakhan":67})
print(dict)

dict.update({"werd":67})
print(dict)

#remove key-value

dict.pop("werd")
print(dict)

dict.pop("Arvind")
print(dict)

dict.popitem()
print(dict)

dict.update({"Ajay" : 90})
print(dict)

dict.popitem()
print(dict)


##get all keys from dictionary

for key in dict:
    print(key)

#values

for values in dict.values():
    print(values)

#get k-v pair

for key, values in dict.items():
    print(key, values)

#to check specific key in dict

print("Lakhan" in dict)
print("Monu1" in dict)
dct = {'Arjun':23, "Vandana":30, "Balchand":25, "X":'Mohan'}
dct["X"] = 'Patel'
print(dct)
print(dct["Balchand"])
dct['X'] = 'Mohan Bai'
print(dct)
dct["Y"] = 'Mona'
print(dct)
dct["Z"] = 'Patel'
print(dct)
dct.popitem()
print(dct)
print("Arjun" in dct)

allKeys = dct.keys()
for key in allKeys:
    print(key)

allValues = dct.values()
for values in allValues:
    print(values)

allKeysAndValues = dct.items()
for key, value in allKeysAndValues:
    print("Key:",key, "Value:",value)
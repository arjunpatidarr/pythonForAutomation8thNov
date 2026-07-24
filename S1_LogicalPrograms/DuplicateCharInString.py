x = "abcdefedacbwr"
dict = {}
print(len(x))
print(x.count(x))
for key in x:
    if dict.__contains__(key):
        dict[key] = dict[key] + 1
    else:
        dict[key] = 1

print("find occurence of each word")

for key in dict:
    print(dict[key], key)

print("find duplicate char")

for key in dict:
    if dict[key] > 1:
        print(dict[key], key)

print("find Unique Char")

for key in dict:
    if dict[key] == 1:
        print(dict[key], key)



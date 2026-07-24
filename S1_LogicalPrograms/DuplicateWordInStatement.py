
stat = "India is my country and I love my India"
allWords = stat.split(" ")
print(allWords)
dict = {}

for word in allWords:
    if dict.__contains__(word):
        dict[word] = dict[word]+1
    else:
        dict[word]=1

print("find occurance of each word")

for key in dict:
    print(key,dict[key])

print("find duplicate words")
for key in dict:
    if dict[key]!=1:
        print(key)

print("find unique words")

for key in dict:
    if dict[key] ==1:
        print(key, dict[key])

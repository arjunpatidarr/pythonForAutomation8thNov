inp = "my name is abc"   #"abc is name my"
breakk = inp.split()
print(breakk)
# breakk.reverse()
rev_List = []
for i in range(len(breakk)-1, -1, -1):
    rev_List.append(breakk[i])
print(rev_List)

org = " ".join(rev_List)
print(org)

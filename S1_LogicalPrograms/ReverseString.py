
strg = "abcdefgh"
rev =strg[::-1]
print(rev)


strg1 = "abcde"
rev = ""
for i in range(len(strg1)):  #0<5 #1<5   orr > #for i in OrginalString:  rev = i +rev
    rev = strg1[i]+rev  #edcba

print(rev)
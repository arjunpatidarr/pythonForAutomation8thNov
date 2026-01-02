
s1 = "Velocity"

print(len(s1))
s1 = s1.upper()
print(s1.upper())

s1 = s1.lower()
print(s1)

s2 = ["abc", 23,45,6,12,4,23,45,2,23]
print(s2.count(23))

#compare two string

l1 = "abcdefgh"
l2 = "ABCDEFGH"
print(l1==l2)

l2 = l2.lower()
print(l1==l2)
print(l1.__eq__(l2))

l2 = l2.upper()

#compare data no need to compare case
print(l1.lower()==l2.lower())
print(l1.upper()==l2.upper())

t1 = "My name is Arjun"
print("Arjun" in t1)
print("MY" in t1)

print(t1.__contains__("is"))
print(t1.__contains__("IS"))

#check starting part of string
t2 = "I'm graduated from symbiosis international university"

print(t2.startswith("Im"))
print(t2.startswith("I"))

#check ending part of string

print(t2.endswith("ty"))
print(t2.endswith("l"))

#to check any specific char by index
print(t2[23])
print(t2[30])
print(t2[35])
print(len(t2))

#to get multiple character  by index
print("------")
print(t2[0:5])
print(t2[4:10])



#to check specific index of any char by passing char
print("-----")
t3 = "abcdefghiabcdefghi"
print(len(t3))
print(t3.find("e"))
print(t3.rfind("i"))
print(t3[0])
t4="abcdef"
print(len(t4))

#alternative method of find

print(t4.find("c"))
print(t4.find("f"))

#to combine two string or concetination

print(t3+t4)
print(t2+t3+t4)

#to remove white space from the left and right side of string
t5 = "  hi i'm from kota rajasthan  "
#t5 = t5.strip()
print(t5)
print(t5.lstrip())
print(t5.rstrip())

#to change and replace of substring
#for temporary replace
print(t5.replace(" ", ""))
print(t5.replace ("hi", "HI"))





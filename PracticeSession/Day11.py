s = "I am learning automation testing Using python"
s1 = "   "
s2 ="I'm 27 year old"

print(len(s))
print("-------------------")
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
#check alpha, number, both combine
print("------------------")
print(s2.isalnum())
print(s.isnumeric())
print(s.isalpha())
#space
print("------------------")
print(s.isspace())
print(s1.isspace())

print("-----------------------")
sr = "python3 is8 not0"
print(sr.isalnum())
a1 = "Python1"
a2 = "python1"
print(a1==a2)
print(a1.lower()==a2.lower())
print(a1.__eq__(a2))

print("---------------------")
s5 = "I'm using py robot framework with python"
print(s5.find("p"))
print(s5.rfind("p"))

print(s5.index("p"))
print(s5.find("y"))
print(s5[0:3])
print(s5[0])

print(s5.startswith(("I'm")))
print(s5.lower().startswith("i'm"))
print(s5.endswith("python"))

s6 = " python   "
print(s6)
print(s6.strip())
print(s6.rstrip())
print(s6.lstrip())
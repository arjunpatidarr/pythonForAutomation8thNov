
#strings and it's methods
#string is inmutable

s1 = "velocity"
s2 ="i'm learning Python for Automation"
print(len(s1))
print(len(s2))
print(s1.upper())
print(s1.lower())
#s1 = s1.upper()
print(s1)
print(s2.capitalize())
#print(s1)
print(s2.title())
#find index by passing text or word or sentence
print(s2.find("i'm"))
print(s2.find("learning"))
print(s2.find("Python"))
print(s2.index("i'm"))
print(s2.index("learning"))

s3 = "I'm from kota rajasthan India"
print(s3.index("I"))
print(s3.rfind("I"))
s4 = " Lakhan  Bhaiya "
print(s4.strip())
print(s4.lstrip())
print(s4.rstrip())
s5 = "I'mfromIndiaI'mfromIndia"
print(s5.startswith("I'm"))
print(s5.endswith("India"))
print(s5.startswith("from"))

print("----------------")
s6 = "we are automation tester"
print(s6.isalpha())
print(s5.isalpha())
s7 = "12345676Rahul@#$aer"
print(s7.isnumeric())
print(s7.isalnum())


print(s6.replace("tester", "QA Engineer"))
s6 = s6.replace("tester", "QA Engineer")
print(s6)

s8 = " you are from mumbai "
print(s8.replace(" ", ""))
s9 = "you are belongs from pune"
print(s8==s9)
print(s8.__eq__(s9))
print("belongs" in s9)
print(s9.__contains__("belongs"))

print(s9[0:3])








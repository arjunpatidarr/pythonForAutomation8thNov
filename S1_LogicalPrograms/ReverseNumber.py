#appr 1

# num = 12345
#
# str = str(num)
# rev = str[::-1]
# rev = int(rev)
# print(rev)





#appr 2
num =12345
rev = 0
while num>0:
    rem = num%10  #5
    rev = rev*10 +rem
    num = num//10  #1234

print(rev)



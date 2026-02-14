num =153
Orgnum = num
sum =0

while num>0:   #153>0  #15>0
    rem = num%10   #3   #5
    sum = sum + rem*rem*rem  #0+27 = 27 +125
    num = num//10     #15


if Orgnum == sum:
    print("Given number is Armstrong")
else:
    print("Given number is not Armstrong")
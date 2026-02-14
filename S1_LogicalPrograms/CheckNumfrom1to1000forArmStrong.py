#Check ArmStrongNumberFrom 1 to 1000
for i in range(1,1001):
    num = i
    OrgNum = num
    sum =0
    while num>0:
        rem = num%10
        sum = sum+rem*rem*rem
        num = num//10

    if OrgNum == sum:
        print("ArmStrongNumber", i)
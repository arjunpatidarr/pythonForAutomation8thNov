#
# i = 1
# while True:
#     if i % 3 == 0:  #2%3 ==0
#         break
#     print(i)
#     #i +=1
#     i = i+1
from operator import truediv

#Write a loop that prints numbers starting from 1 and stops (breaks) when it encounters the first even number greater than 5.

i = 1
while True:
    if i%2==0:
        #print("if body" , i)
        if i>5:
        # print("i>5",i)
         print("condition is true", i)
         break
    #print(i)
    i = i+1

#or

i=1
while True:
    if i%2==0 and i>5:
        print("condition is true", i)
        break
    i = i+1


#Create a program that continuously asks the user to "Enter a number (0 to stop)". The loop should only break if the user enters 0

# while True:
#    i = int(input("Enter a number: "))
#    if i ==0:
#        break
#    print(i)

#Write a while loop that starts at 10 and decreases by 1 each time. The loop should print the numbers but break immediately if the number becomes 3.
print("-----------")
i = 10
while True:
    if i==3:
        print("condition is true", i)
        break
    print(i)
    i = i-1

#Write a loop that starts at i = 5 and increments by 1. The loop should print each number but must break once it reaches a number that is perfectly divisible by both 3 and 4

print("-------------------------------")
i = 5
while True:
    if i%3==0 and i%4 ==0:
        print("condition is true", i)
        break
    i = i+1

#Write a loop that prints numbers from 1 to 10, but skips any number that is a multiple of 7.
print("--------------")
i = 0
while True:
    i=i+1
    if i%7==0:
        print("condition is true", i)
        continue
    print(i)
    if i ==10:
        break

print("___________________________")
for i in range(0,11):
    if i%7==0:
        print("multiple of 7 is ", i)
    print(i)



i = 0
while True:
    i +=1
    if i%2==0:
        continue
    if i ==10:
        break
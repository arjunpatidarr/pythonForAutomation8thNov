

#print a num from 1 to 10

#1)for loop

for i in range(1, 10, 1):  #9<10 #10<10
    print(i)


#) print even num from 1 to 50

for i in range(2, 51, 2):
    print(i)


#decrement

#print odd numbers  13 to 1

# for i in range(13, 0, -2): #startnum>endnum  13>11
#     print(i)
#
# my_string = "Python"
#  # Loop through the characters
# for i in my_string:
#     print(i)


#print square of num from 11 to 20
print("-----------")
# for i in range(11, 21, 1):
#     print(i*i)
#     print(i**2)



# my_string = "World"
# # Loop using index
# for i in range(len(my_string)):
#     # Access the character using the index
#     print(f"Character at index {i} is {my_string[i]}")
#
# String = "aAVCBXDGSaAaQNWBW"
# #duplicate character
# for i in range(String):
#
#     print(String.count(i))
#
# print("print table using for loop")
# table = int(input("Enter a number: "))
# for i in range(1, 11, 1):
#       print(i*table)

print("print table using while loop")

#startNum
#while  condition:
#while body
#incr/decr

table = int(input("Enter a number: "))
number =1
while number<11:
    print(number*table)
    number = number+1











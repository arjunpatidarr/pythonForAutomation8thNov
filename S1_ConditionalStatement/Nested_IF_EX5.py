# Nested if for eligibility:
# Write a Python program that takes a person's age and whether they have a driver's license (True/False) as input.
# If the person is 18 or older:
# If they have a driver's license, print "Eligible to drive."
# Else, print "Eligible to get a driver's license."
# Else (if younger than 18), print "Not eligible to drive yet."


age = 90
DrivingLicenece = True
if age>=18:
    if DrivingLicenece==True:
        print("Eligible to drive")
    else:
        print("Eligible to get a driver's licenece")
else:
    print("Not eligible to drive yet")

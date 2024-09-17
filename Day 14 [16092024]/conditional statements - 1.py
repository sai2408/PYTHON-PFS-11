#Conditional statements
#If
#Problem - 1
#Approach - 1
'''
a = int(input("enter a number: "))
even = [0,2,4,6,8]
x = a%10
if x in even:
    print("even number")
print("Outside if structure")
'''
#Approach -2
'''
a = int(input("enter a number: "))
if (a%2 == 0):
    print("even number")
print("Outside if structure")
'''
#If - Else
#Problem - 2
#Approach - 1
'''
a = int(input("enter a number: "))
even = [0,2,4,6,8]
x = a%10
if x in even:
    print("even number")
else:
    print("Odd number")
print("Outside if structure")
'''
#Approach - 2
'''
a = int(input("enter a number: "))
if (a%2 == 0):
    print("even number")
else:
    print("Odd number")
print("Outside if structure")
'''
#Elif
#Problem - 3
'''
age = int(input("Enter your age: "))
vc = input("Do you have Voter card (y/n): ")
if (age>=18 and vc=="y"):
    print("Can vote")
elif (age>=18 and vc =="n"):
    print("Voter card should be there")
else:
    print("Can not Vote")
'''
#Nested
#Problem - 4
'''
age = int(input("Enter your age: "))
vc = input("Do you have Voter card (y/n): ")
if age>=18:
    if vc=="y":
        print("Yes you can vote")
    else:
        print("Need Voter card")
else:
    if vc == "y":
        print("Can vote but not eleigible")
    else:
        print("Can not vote")
'''
#Conditional Expression
'''
age = int(input("Enter your age: "))
x = 'Can vote' if age >= 18 else "Can not vote"
print(x)
'''












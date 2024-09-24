#Problem - 1
#Approach- 1
'''
fname = input("enter your first name: ")
lname = input("enter your last name: ")
print(f"{lname}, {fname}")
'''
#Approach- 2
'''
fname = input("enter your first name: ")
lname = input("enter your last name: ")
print("{}, {}".format(lname,fname))
'''
#Problem - 2
#Approach - 1
'''
name = input("enter your full name: ")
x = name.title()
print(f"Hello, {x}")
'''
#Approach - 2
'''
name = input("enter your full name: ")
x = name.title()
print("Hello, {}".format(x))
'''
#Problem - 3
'''
x = float(input("Enter a floating-point number: "))
print("{:.2f}".format(x))
'''
#Problem - 4
#Appraoch - 1
'''
n1 = int(input("enter an integer: "))
n2 = float(input("enter a float: "))
n3 = input("enter a string: ")
print(f"{n1}, {n2}, {n3}")
'''
#Approach - 2
'''
n1 = int(input("enter an integer: "))
n2 = float(input("enter a float: "))
n3 = input("enter a string: ")
print("{}, {}, {}".format(n1,n2,n3))
'''
#Problem - 5
'''
year = int(input("enter your birth year: "))
age = 2024-year
print(age)
'''
#Problem - 6
#Approach - 1
'''
n1 = int(input("enter first number: "))
n2=  int(input("enter second number: "))
print("The numbers you entered are",n1,"and",n2)
'''
#Approach - 2
'''
n1 = int(input("enter first number: "))
n2=  int(input("enter second number: "))
print(f"The numbers you entered are {n1} and {n2}")
'''
#Approach - 3
'''
n1 = int(input("enter first number: "))
n2=  int(input("enter second number: "))
print("The numbers you entered are {} and {}".format(n1,n2))
'''
#Problem - 7
#Approach- 1
'''
name = input("enter product name: ")
price = int(input("enter product price: "))
print("Product:",name)
print("Price: ",price)
'''
#Approach - 2
'''
name = input("enter product name: ")
price = int(input("enter product price: "))
print(f"Product: {name}" )
print(f"Price:  {price}")
'''
#Approach - 3
'''
name = input("enter product name: ")
price = int(input("enter product price: "))
print("Product: {}".format(name) )
print("Price:  {price}".format(price))
'''
#Problem - 8
#Approach - 1
'''
s = input("enter sentence")
n = len(s)
x = s.count(" ")
print("Your sentence:",s)
print("Character count (excluding spaces):",(n-x))
'''
#Approach - 2
'''
s = input("enter sentence")
n = len(s)
x = s.split()
x = len(x)
spaces = x - 1
print("Your sentence:",s)
print("Character count (excluding spaces):",(n-spaces))
'''










#Text type
#string
'''
s1 = str(input())
print(s1)
print(type(s1))
s2 = input()
print(s2)
print(type(s2))
s3,s4 = input().split()
print(s3)
print(s4)
s5,s6 = input().split(",")
print(s5)
print(s6)
uname = input("Enter Username: ")
pwd = input("Enter Password: ")
print(pwd)
print(uname)
s5,s6 = input("Enter a,b values splitting with comma : ").split(",")
print(s5)
print(s6)
'''
#Numeric Data Type
#Int
'''
a1 = int(input("enter a value: "))
print(a1)
print(type(a1))
a1 = int(input("Enter A value: "))
a2 = int(input("Enter B value: "))
print(a1)
print(a2)
a1,a2 = map(int,input().split())
print(a1)
print(a2)
a1,a2,a3,a4 = map(int,input("Enter Domain Address: ").split("."))
print(a1)
'''
#Float
'''
a1 = float(input())
print(a1)
print(type(a1))
a2 = float(input("enter A1 Value: "))
print(a2)
a1,a2 = map(float,input().split())
print(a1)
print(a2)
a1,a2,a3 = map(float,input("enter three value: ").split(","))
print(a1)
print(a2)
print(a3)
'''
#Complex
'''
a1 = complex(input())
print(a1)
print(type(a1))
a1 = complex(input("enter Complex value: "))
print(a1)
print(type(a1))
'''
#Sequential Data Type
#List
'''
x = [10,20,30,40,50]
print(x)
print(type(x))
x = list(map(int,input().split()))
print(x)
print(type(x))
x1 = input().split()
print(x1)
x = list(map(float,input().split()))
print(x)
x = list(map(int,input().split(",")))
print(x)
'''
#Tuple
'''
x = (10,20,30,40,50)
print(x)
print(type(x))
x = tuple(map(int,input().split()))
print(x)
print(type(x))
x = tuple(map(float,input().split()))
print(x)
'''
#Problem
'''
n = int(input())
x = list(map(int,input().split()))
x = x[:n]
print(x)
'''




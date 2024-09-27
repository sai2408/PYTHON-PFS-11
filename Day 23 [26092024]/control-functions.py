#Problem - 1 [NXM] [Sum of Matrix]
'''
n => 3
1 2 3
4 5 6
7 8 9
1 1 1
2 2 2
0 0 0
-----
2 3 4
6 7 8
7 8 9
'''
#Approach
'''
m1 = []
m2 = []
n = int(input())
for i in range(n):
    x = list(map(int,input().split()))
    m1.append(x)
for i in range(n):
    x = list(map(int,input().split()))
    m2.append(x)
res = []
x1 = []
for i in range(n):
    x1.append(0)
for i in range(n):
    res.append(x1.copy())
for i in range(n):
    for j in range(n):
        res[i][j] = m1[i][j] + m2[i][j]
for i in res:
    print(*i)
'''
#Functions
#BUilt in functions
'''
print(abs(100))
x = abs(-100)
print(x)
print(bin(10))
print(hex(64))
print(oct(64))
print(ord('A'))
print(chr(65))
for i in range(200):
    print(f"{i} -> {chr(i)}")
print(eval("10+20-10"))
'''
#User - Defined Function
#WPWR
'''
def fun1(num1,num2):
    v1 = num1+num2
    v2 = num1-num2
    v3 = num1*num2
    v4 = num1%num2
    return v1,v2,v3,v4
x = int(input("enter first number: "))
y = int(input("enter second number: "))
r1,r2,r3,r4 = fun1(x,y)
print(r1)
print(r2)
print(r3)
print(r4)
'''
#WPWOR
'''
def fun1(num1,num2):
    v1 = num1+num2
    v2 = num1-num2
    v3 = num1*num2
    v4 = num1%num2
    print(v1)
    print(v2)
    print(v3)
    print(v4)
x = int(input("enter first number: "))
y = int(input("enter second number: "))
fun1(x,y)
'''
#WOPWR
'''
def fun1():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    v1 = num1+num2
    v2 = num1-num2
    v3 = num1*num2
    v4 = num1%num2
    return v1,v2,v3,v4
r1,r2,r3,r4 = fun1()
print(r1)
print(r2)
print(r3)
print(r4)
'''
#WOPWOR
'''
def fun1():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    v1 = num1+num2
    v2 = num1-num2
    v3 = num1*num2
    v4 = num1%num2
    print(v1)
    print(v2)
    print(v3)
    print(v4)
fun1()
'''













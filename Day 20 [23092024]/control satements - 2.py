#Problem - 1
#Approach - 1
'''
num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
'''
#Approach - 2
'''
num = int(input("Enter a number: "))
c = 0
for i in range(1,num+1):
    if num%i == 0:
        c = c + 1
if c == 2:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.") 
'''
#Problem - 2
#APproach - 1
'''
n = int(input("Enter the number: "))
res = 0
if n >= 0:
    while n > 0:
        r = n%10
        res = (res*10) + r
        n = n // 10
else:
    n = -1 * n
    while n > 0:
        r = n%10
        res = (res*10) + r
        n = n // 10
    res = -1 * res
print(res)
'''
#Approach - 2
'''
n = int(input("enter your number: "))
if n >= 0:
    x = str(n)
    x = x[::-1]
    x = int(x)
    print(x)
else:
    n = n * -1
    x = str(n)
    x = x[::-1]
    x = int(x)
    x = -1 * x
    print(x)
'''
#Appraoch - 3
'''
n = int(input("enter your number: "))
if n >= 0:
    x = str(n)
    x = x[::-1]
    print(x)
else:
    n = n * -1
    x = str(n)
    x = x[::-1]
    x = "-" + x
    print(x)
'''
#Problem - 3 [ Factorial ]
#Approach - 1
'''
n = int(input())
x = 1
for i in range(1,n+1):
    x = x * i
print(x)
'''
#Approach - 2
'''
n = int(input())
x = 1
while n > 1:
    x = x * n
    n = n - 1
print(x)
'''
#Problem - 4 [ Adding number before and after the value ]
#Approach - 1
'''
n1 = int(input("Enter main number: "))
n2 = int(input("enter number to be added last and first : "))
#print(n1)
n1 = (n1 * 10) + n2
#print(n1)
res = 0
while n1 > 0:
    r = n1%10
    res = (res*10) + r
    n1 = n1 // 10
#print(res)
res = (res * 10) + n2
#print(res)
res1 = 0
while res > 0:
    r = res%10
    res1 = (res1*10) + r
    res = res // 10
print(res1)
'''
#Approach - 2
'''
n1 = input("Enter main number: ")
n2 = input("enter number to be added last and first : ")
res = n2 + n1 + n2
print(res)
'''
#Problem - 5














    
    



















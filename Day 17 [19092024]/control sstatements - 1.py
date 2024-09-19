#Problem - 1
#Approach - 1
'''
a = [10,20,30,40,50]
n = len(a)
for i in range(n):
    print(a[i])
'''
#Approach - 2
'''
a = [10,20,30,40,50]
for i in a:
    print(i)
'''
#Problem - 2
'''
s = {1,2,3,4}
for i in s:
    print(i)
'''
#Problem - 3
'''
d = {1:10,2:20,3:30,4:40}
for i in d:
    print(i,d[i])
'''
#Problem - 4
#Approach -1
'''
s = "sai vardhan"
for i in range(len(s)):
    print(s[i])
'''
#Approach - 2
'''
s = "Sai vardhan"
for i in s:
    print(i)
'''
#Problem - 5
#For loop
'''
for i in range(1,101):
    print(i)
'''
#While Loop
'''
n = 1
while n <= 100:
    print(n)
    n = n + 1
'''
#Problem - 6
#For loop
#Approach - 1
'''
for i in range(2,101,2):
    print(i)
'''
#Approach - 2
'''
for i in range(1,101):
    if i%2==0:
        print(i)
'''
#While Loop
#Appraoch - 1
'''
n = 2
while n<=100:
    print(n)
    n = n + 2
'''
#Approach - 2
'''
n = 1
while n<=100:
    if n%2==0:
        print(n)
    n = n + 1
'''
#Problem - 7
#For loop
#Approah - 1
'''
start = int(input("enter starting value: "))
end = int(input("enter ending value: "))
es = 0
os = 0
for i in range(start,end+1):
    if i%2==0:
        es = es + i
    else:
        os = os + i
avg = (es+os)/2
print(avg)
'''
#Approach - 2
'''
start = int(input("enter starting value: "))
end = int(input("enter ending value: "))
es = []
os = []
for i in range(start,end+1):
    if i%2 == 0:
        es.append(i)
    else:
        os.append(i)
avg = (sum(es)+sum(os))/2
print(avg)
'''
#While Loop
#Approach - 1
'''
start = int(input("enter starting value: "))
end = int(input("enter ending value: "))
es = 0
os = 0
while start <= end:
    if start%2 == 0:
        es = es + start
    else:
        os = os + start
    start = start + 1
avg = (es+os)/2
print(avg)
'''
#Approach - 2
'''
start = int(input("enter starting value: "))
end = int(input("enter ending value: "))
es = []
os = []
while start<=end:
    if start%2 == 0:
        es.append(start)
    else:
        os.append(start)
    start += 1
avg = (sum(es)+sum(os))/2
print(avg)
'''
#Problem - 8
#Approach - 1
'''
x = list(map(int,input().split()))
for i in range(1,101):
    if i not in x:
        print(i)
        break
'''
#Approach - 2
'''
x = list(map(int,input().split()))
x.sort()
for i in range(1,101):
    if i != x[i-1]:
        print(i)
        break
'''
#Problem - 9
#Approach - 1 [For loop]
'''
t = int(input())
for i in range(t):
    n = int(input())
    if n > 98:
        print("Yes")
    else:
        print("No")
'''
#Approach - 2 [While loop]
'''
t = int(input())
while t>0:
    n = int(input())
    if n>98:
        print("Yes")
    else:
        print("No")
    t = t - 1
'''
#Problem - 10
'''
t = int(input())
for i in range(t):
    tc = 0
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(n):
        if a[i] >= x:
            tc = tc + b[i]
    print(tc)
'''
            
        



































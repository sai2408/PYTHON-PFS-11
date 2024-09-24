#Problem - 1
'''
t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    x = a-c
    y = b-d
    if x > y:
        print("Second")
    elif x < y:
        print("first")
    else:
        print("Any")
'''
#Problem - 2
#Approach- 1
'''
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    if x >= n:
        print(0)
    else:
        a = n - x
        if (a%4==0):
            print((a//4))
        else:
            print((a//4)+1)
'''
#Approach-2
'''
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    if x >= n:
        print(0)
    else:
        a = n - x
        y = (a + 3)//4
        print(y)
'''
#Approach - 3
'''
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    pc = 0
    if x >= n:
        print(0)
    else:
        while x < n:
            x = x + 4
            pc = pc + 1
        print(pc)
'''
#Problem - 3
#Approach - 1
'''
t = int(input())
for i in range(t):
    n = int(input())
    tc = n * 50
    s1 = tc * 0.2
    s2 = tc * 0.2
    s3 = tc * 0.3
    ts = (s1+s2+s3)
    print(int(tc-ts))
'''
#Approach - 2
'''
t = int(input())
for i in range(t):
    n = int(input())
    tc = n*50
    ts = tc*0.7
    print(int(tc-ts))
'''























        

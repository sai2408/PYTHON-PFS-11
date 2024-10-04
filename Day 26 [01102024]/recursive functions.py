#Recursive functions
#Problem - 1 [ 10 - 1 ]
#Appporach - 1
'''
n = 10
while n > 0:
    print(n)
    n = n - 1
'''
#Appraoch - 2
'''
def abc(x):
    if x > 0:
        print(x)
    else:
        return
    abc(x-1)
n = 10
abc(n)
'''
#Problem - 2 [1 - 10]
#Appraoch - 1
'''
n = 1
while n <= 10:
    print(n)
    n = n + 1
'''
#Approach - 2
'''
def xyz(x):
    if x <= 10:
        print(x)
    else:
        return
    xyz(x+1)
n = 1
xyz(n)
'''
#Problem - 3 [ Factorial Value ]
#Approach - 1
'''
n = 4
res = 1
while n > 0:
    res = res * n
    n = n - 1
print(res)
'''
#Appraoch - 2
'''
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
x = 4
res = fact(x)
print(res)
'''
#Problem - 4 [series from n - m]
#Approach - 1
'''
st = 24
end = 56
while st <= end:
    print(st)
    st = st + 1
'''
#Approach - 2
'''
def mno(a,b):
    if a <= b:
        print(a)
    else:
        return
    mno(a+1,b)
st = 24
end = 56
mno(st,end)
'''
















































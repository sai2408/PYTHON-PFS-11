#Required argumnets
'''
def abc(a,b,c):
    c = a + b + c
    print(c)
abc(10,20,30)
'''
#Default Argumnets
'''
def abc(a=0,b=0,c=0):
    c = a + b + c
    print(c)
abc(10,20,30)
abc(10,20)
abc(10)
abc()
'''
#Keyword Argumnets
'''
def abc(a,b,c):
    print(a,b,c)
abc(a=10,b=20,c=30)
abc(c=30,b=20,a=10)
'''
#Varible Number of Argumnets
'''
def abc(*mno):
    c = 0
    for i in mno:
        c = c + i
    print(c)
abc()
abc(1,2)
abc(1,2,3,4)
abc(1,2,3,4,5,6,7)
'''
#Scope of the variables
#Program - 1
'''
a = 10
def abc():
    b = 20
    print(b)
print(a)
abc()
'''
#Program - 2
'''
a = 10
def abc():
    b = 20
    print(a)
    print(b)
print(a)
abc()
'''
#Program - 3
'''
a = 10
def abc():
    b = 20
    global a
    a = 100
    print(b)
print(a)
abc()
print(a)
'''

















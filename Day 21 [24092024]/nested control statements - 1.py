#Symbolic Patterns
#Pattern - 1 [NXN][Complete]
#Approach - 1 [for in for]
'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print("#",end=" ")
    print()
'''
#Approach - 2 [for in while]
'''
n = int(input("enter a number: "))
x = n
while n>0:
    for i in range(x):
        print("#",end=" ")
    print()
    n = n - 1
'''
#Appaoch - 3 [while in while]
'''
n = int(input("enter a number: "))
rows = n
while rows > 0:
    cols = n
    while cols > 0:
        print("#",end=" ")
        cols = cols - 1
    rows = rows - 1
    print()
'''
#Appraoch - 4 [while in for]
'''
n = int(input("enter a number: "))
for i in range(n):
    x = n
    while x > 0:
        print("#",end=" ")
        x = x - 1
    print()
'''
#Pattern - 2 [NXN][Complete]
'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if j%2==0:
            print("#",end=" ")
        else:
            print("@",end=" ")
    print()
'''
#Pattern - 3 [NXN][Complete]
'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if i==j:
            print("@",end=" ")
        else:
            print("#",end=" ")
    print()
'''
#Pattern - 4 [NXN] [Complete]
'''
n = int(input("Enter a number: "))
for i in range(n):
    if i%2 == 0:
        for j in range(n):
            print("#",end= " ")
    else:
        for j in range(n):
            print("@",end=" ")
    print()
'''
#Pattern - 5 [NXM] [Complete]
'''
rows = int(input("enter number of rows: "))
cols = int(input("enter number of columns: "))
for i in range(rows):
    for j in range(cols):
        print("#",end=" ")
    print()
'''
#Assignment
'''
n = 4
# @ # @
@ # @ #
# @ # @
@ # @ #
'''
n = int(input("enter a number: "))
for i in range(n):
    if i%2 == 0:
        for j in range(n):
            if j%2 == 0:
                print("#",end=" ")
            else:
                print("@",end=" ")
    else:
        for j in range(n):
            if j%2 != 0:
                print("#",end=" ")
            else:
                print("@",end=" ")
    print()


























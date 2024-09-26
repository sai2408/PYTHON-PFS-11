#Problem - 1
'''
n => 4
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
'''
#Appraoch - 1 [With Counter]
'''
n = int(input("Enter a number: "))
c = 1
for i in range(n):
    for j in range(n):
        print(f"{c}",end= " ")
    print()
    c = c + 1
'''
#Approach - 2 [Without Counter]
'''
n = int(input("Enter a nuber: "))
for i in range(n):
    for j in range(n):
        print(f"{i+1}",end= " ")
    print()
'''
#Problem - 2
'''
n => 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
'''
#Approach - 1 [With Counter]
'''
n = int(input("Enter a number: "))
for i in range(n):
    c = 1
    for j in range(n):
        print(f"{c}",end=" ")
        c = c + 1
    print()
'''
#Approach - 2 [Without counter]
'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print(f"{j+1}",end=" ")
    print()
'''
#Problem - 3
'''
n => 5
9 2 3 4 5
1 8 3 4 5
1 2 7 4 5
1 2 3 6 5
1 2 3 4 5
'''
#Approach
'''
n = int(input("Enter a number: "))
c2 = 9
for i in range(n):
    c1 = 1
    for j in range(n):
        if i == j:
            print(f"{c2}",end= " ")
            c2 = c2 - 1
        else:
            print(f"{c1}",end= " ")
        c1 = c1 + 1
    print()
'''
#Problem - 4
'''
n => 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
#Approach - 1 [With Counter]
'''
n = int(input("Enter a number: "))
for i in range(n):
    c = 1
    for j in range(n):
        if i>=j:
            print(f"{c}",end=" ")
            c = c + 1
        else:
            print(" ",end=" ")
    print()
'''
#Approach - 2 [Without counter]
'''
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if i>=j:
            print(f"{j+1}",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#Problem - 5
'''
n => 5
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''
#Approach
'''
n = int(input("Enter a number: "))
for i in range(n):
    c = 5
    for j in range(n):
        if i>=j:
            print(f"{c}",end= " ")
            c = c - 1
        else:
            print(" ",end=" ")
    print()
'''
#Problem - 5
'''
n => 5
1
@ @
2 3 4
@ @ @ @
5 6 7 8 9
n => 4
1
@ @
2 3 4
@ @ @ @
'''
#Approach
'''
n = int(input("enter a number: "))
c = 1
for i in range(n):
    if i%2 == 0:
        for j in range(n):
            if i >= j:
                print(f"{c}",end= " ")
                c = c + 1
            else:
                print(" ",end=" ")
    else:
        for j in range(n):
            if i >= j:
                print("@",end= " ")
            else:
                print(" ",end=" ")
    print()
'''
#Problem - 6
'''
n => 5
1
@ @
2 2 2
@ @ @ @
3 3 3 3 3
n => 4
1
@ @
2 2 2
@ @ @ @
'''
#Approach
'''
n = int(input("enter a number: "))
c = 1
for i in range(n):
    if i%2 == 0:
        for j in range(n):
            if i >= j:
                print(f"{c}",end= " ")
            else:
                print(" ",end=" ")
        c = c + 1
    else:
        for j in range(n):
            if i >= j:
                print("@",end= " ")
            else:
                print(" ",end=" ")
    
    print()
'''
#Matrix
#Problem - 7 [NXN]
'''
3
1 2 3
4 5 6
7 8 9
3
1 2 3 4
1 3 4 6
7 4 2 5
1 6 2 6
'''
#Solution
'''
matrix = []
n = int(input("enter size of the matrix: "))
for i in range(n):
    x = list(map(int,input().split()))
    matrix.append(x)
print(matrix)
for i in matrix:
    print(*i)
'''
#Problem - 2 [NXM] [Sum of Matrix]
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
















































































































    



















            

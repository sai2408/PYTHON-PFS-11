#Problem - 1
'''
t = int(input())
for i in range(t):
    s = input()
    for i in range(len(s)-1):
        if s[i] in s[i+1:]:
            print(s[i])
            break
    else:
        print(".")
'''
#Problem - 2
'''
t = int(input())
d = {}
for i in range(t):
    x = input()
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
re1 = max(d.values())
re2 = []
for i in d:
    if d[i] == re1:
        re2.append(i)
print(max(re2),re1)
'''
#Problem - 3
t = int(input())
for i in range(t):
    n = int(input())
    lst = []
    for i in range(n):
        x = int(input())
        lst.append(x)
    for i in lst:
        if lst.count(i) == 1:
            print(i)
            break
#Problem - 4














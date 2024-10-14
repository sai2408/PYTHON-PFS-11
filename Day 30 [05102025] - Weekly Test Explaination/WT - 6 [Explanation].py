#Problem - 1
#Approach - 1
'''
s = input()
x = input()
res = 0
for i in range(len(s)):
    if s[i] == x:
        res = res + 1
print(res)
'''
#Appraoch - 2
'''
s = input()
x = input()
res = 0
for i in s:
    if i == x:
        res = res + 1
print(res)
'''
#Approach - 3
'''
s = input()
x = input()
res = s.count(x)
print(res)
'''
#Problem - 2
#Approach - 1
'''
s = input()
vowels = "aeiouAEIOU"
for i in range(len(s)):
    if s[i] not in vowels:
        print("No")
        break
else:
    print("Yes")
'''
#Approach - 2
'''
s = input()
vowels = "aeiouAEIOU"
for i in s:
    if i not in vowels:
        print("No")
        break
else:
    print("Yes")
'''
#Problem - 1
#Approach - 1
'''
s = input()
digits = "0123456789"
for i in range(len(s)):
    if s[i] not in digits:
        print("No")
        break
else:
    print("Yes")
'''
#Appraoch - 2
'''
s = input()
digits = "0123456789"
for i in s:
    if i not in digits:
        print("No")
        break
else:
    print("Yes")
'''
#Approach - 3
'''
s = input()
if s.isdigit():
    print("Yes")
else:
    print("No")
'''
#Problem - 4
'''
s = input()
res = ""
count = 1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count = count + 1
    else:
        res = res + s[i-1]
        res = res + str(count)
        count = 1
res =res + s[-1]
res = res + str(count)
print(res)
'''





























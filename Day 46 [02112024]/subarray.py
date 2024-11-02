#Sub array
'''
arr = [1,2,3,4]
n = len(arr)
res = []
for i in range(n):
    for j in range(i+1,n+1):
        res.append(arr[i:j])
print(res)
'''
#sub Sequence
'''
def getsub(arr,ind=0,sub=None,res=None):
    if sub is None:
        sub = []
    if res is None:
        res = []
    if ind == len(arr):
        res.append(sub)
        return res
    getsub(arr,ind+1,sub,res)

    getsub(arr,ind+1,sub+[arr[ind]],res)

    return res
arr = [1,2,3]
mainres = getsub(arr)
print(mainres)
'''
#Problem - 1 [ Longest subarray with product == target ]
'''
arr = [1,2,3,4]
t = 6
n = len(arr)
res = []
for i in range(n):
    for j in range(i+1,n+1):
        res.append(arr[i:j])
print(res)
res1 = []
for arr in res:
    x = 1
    for i in arr:
        x = x * i
    if x == t:
        res1.append(arr)
print(res1)
mlen = 0
for i in res1:
    mlen = max(mlen,len(i))
count = 0
for i in res1:
    if len(i) == mlen:
        count = count + 1
print(count)
'''
#Problem - 2 [ Shortest subarray with product == target ]
'''
arr = [1,2,3,4]
t = 6
n = len(arr)
res = []
for i in range(n):
    for j in range(i+1,n+1):
        res.append(arr[i:j])
print(res)
res1 = []
for arr in res:
    x = 1
    for i in arr:
        x = x * i
    if x == t:
        res1.append(arr)
print(res1)
mlen = n
for i in res1:
    mlen = min(mlen,len(i))
count = 0
for i in res1:
    if len(i) == mlen:
        count = count + 1
print(count)
'''
#Problem - 3 [ Longest subarray with sum == target ]
'''
arr = [1,2,3,4]
t = 6
n = len(arr)
res = []
for i in range(n):
    for j in range(i+1,n+1):
        res.append(arr[i:j])
print(res)
res1 = []
for ar in res:
    x = sum(ar)
    if x == t:
        res1.append(ar)
print(res1)
mlen = 0
for i in res1:
    mlen = max(mlen,len(i))
count = 0
for i in res1:
    if len(i) == mlen:
        count = count + 1
print(count)
'''
#Problem - 4 [ Shortest subarray with sum == target ]
'''
arr = [1,2,3,4]
t = 6
n = len(arr)
res = []
for i in range(n):
    for j in range(i+1,n+1):
        res.append(arr[i:j])
print(res)
res1 = []
for ar in res:
    x = sum(ar)
    if x == t:
        res1.append(ar)
print(res1)
mlen = n
for i in res1:
    mlen = min(mlen,len(i))
count = 0
for i in res1:
    if len(i) == mlen:
        count = count + 1
print(count)
'''
#Problem - 5 [ Largest subsequence with product == target ]
'''
def getsub(arr,ind=0,sub=None,res=None):
    if sub is None:
        sub = []
    if res is None:
        res = []
    if ind == len(arr):
        res.append(sub)
        return res
    getsub(arr,ind+1,sub,res)

    getsub(arr,ind+1,sub+[arr[ind]],res)

    return res
arr = [1,2,3,4]
res = getsub(arr)
res1 = []
t = 6
for arr in res:
    x = 1
    for i in arr:
        x = x * i
    if x == t:
        res1.append(arr)
print(res1)
mlen = 0
for i in res1:
    mlen = max(mlen,len(i))
count = 0
for i in res1:
    if len(i) == mlen:
        count = count + 1
print(count)
'''
#Problem - 6 [ Shortest subsequence with product == target ]
'''
def getsub(arr,ind=0,sub=None,res=None):
    if sub is None:
        sub = []
    if res is None:
        res = []
    if ind == len(arr):
        res.append(sub)
        return res
    getsub(arr,ind+1,sub,res)

    getsub(arr,ind+1,sub+[arr[ind]],res)

    return res
arr = [1,2,3,4]
n = len(arr)
res = getsub(arr)
res1 = []
t = 6
for arr in res:
    x = 1
    for i in arr:
        x = x * i
    if x == t:
        res1.append(arr)
print(res1)
mlen = n
for i in res1:
    mlen = min(mlen,len(i))
count = 0
for i in res1:
    if len(i) == mlen:
        count = count + 1
print(count)
'''
#Problem - 7 [ Largest subsequence with sum == target ]
'''
def getsub(arr,ind=0,sub=None,res=None):
    if sub is None:
        sub = []
    if res is None:
        res = []
    if ind == len(arr):
        res.append(sub)
        return res
    getsub(arr,ind+1,sub,res)

    getsub(arr,ind+1,sub+[arr[ind]],res)

    return res
arr = [1,2,3,4]
res = getsub(arr)
print(res)
res1 = []
t = 6
for ar in res:
    x = sum(ar)
    if x == t:
        res1.append(ar)
print(res1)
mlen = 0
for i in res1:
    mlen = max(mlen,len(i))
count = 0
for i in res1:
    if len(i) == mlen:
        count = count + 1
print(count)
'''
#Problem - 8 [ Shortest subsequence with sum == target ]
'''
def getsub(arr,ind=0,sub=None,res=None):
    if sub is None:
        sub = []
    if res is None:
        res = []
    if ind == len(arr):
        res.append(sub)
        return res
    getsub(arr,ind+1,sub,res)

    getsub(arr,ind+1,sub+[arr[ind]],res)

    return res
arr = [1,2,3,4]
res = getsub(arr)
n = len(arr)
print(res)
res1 = []
t = 6
for ar in res:
    x = sum(ar)
    if x == t:
        res1.append(ar)
print(res1)
mlen = n
for i in res1:
    mlen = min(mlen,len(i))
count = 0
for i in res1:
    if len(i) == mlen:
        count = count + 1
print(count)
'''
#Problem - 9
'''
arr = [10,3,5,6,2]
[180,600,360,300,900]
'''
#Appraoch - 1
'''
arr = [10,3,5,6,2]
res = []
n = len(arr)
for i in range(n):
    x = 1
    for j in range(n):
        if i == j:
            pass
        else:
            x = x * arr[j]
    res.append(x)
print(res)
'''
#Appraoch - 2
'''
arr = [10,3,5,6,2]
n = len(arr)
res = []
x = 1
for i in arr:
    x = x * i
print(x)
for i in arr:
    c = x//i
    res.append(c)
print(res)
'''














            
        
















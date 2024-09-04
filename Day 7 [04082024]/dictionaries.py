#Dictionary
#Creation
'''
#Homogeneous
d1 = {}
print(d1)
print(type(d1))
d2 = {1:10,"abc":500,45:45.67}
print(d2)
print(type(d2))
#Hetrogeneous
'''
#Accessing
'''
#Indexing
d = {1:10,2:20,3:30}
print(d[2])
#Methods
#get()
d = { 1:10,2:20,3:30,4:40,5:50}
#keys()
print(d.keys())
#copy()
d1 = d.copy()
print(d1)
#values()
print(d.values())
#items()
print(d.items())
#Looping
'''
#Inserting
'''
#Indexing
d = {1:5,2:20,3:30}
print(d)
d[1] = 10
print(d)
#methods
#update()
d = {1:10,2:20,3:30}
print(d)
d.update({4:40,5:50})
print(d)
#setdefault()
d = {1:10,2:20,3:30}
print(d)
d.setdefault(4,40)
print(d)
#fromkeys()
x = {10,20,50,30,70}
print(x)
d = dict.fromkeys(x,100)
print(d)
'''
#Deleting
'''
#Indexing
d = {1:10,2:20,2.5:25,3:30}
print(d)
del d[2.5]
print(d)
del(d)
print(d)
#methods()
#pop()
d = {1:10,2:20,3:30}
print(d)
d.pop(2)
print(d)
#popitem()
d = {1:10,2:20,3:30,4:40}
print(d)
d.popitem()
print(d)
#clear()
d = {1:10,2:20,3:30}
print(d)
d.clear()
print(d)
'''
#Updating
'''
#Indexing
d = {1:10,2:20,3:30,4:40}
print(d)
d[2] = 25
print(d)
#methods
#update()
d = {1:10,2:20,3:30}
print(d)
d.update({3:35})
print(d)
#setdefault()
d = {1:10,2:20,3:30}
print(d)
'''
#Nested Dictionary
'''
emp = {'name':'sai','salary':60000,'dob':[24,8,24]}
print(emp)
print(emp['name'])
print(emp['dob'][2])
'''









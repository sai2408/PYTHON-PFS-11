#Lists
#Creation
#Homogeneous
'''
a = [10,20,30,40,50]
print(a)
b = [10,"Python",45.24,True,False]
print(b)
c = [10,[10,20,30],56,"abc"]
print(c)
'''
#Hetrogeneous X
#Accessing
#Indexing
'''
a = [10,20,30,40]
print(a[1])
print(a[-2])
b = [10,"Hello",45]
print(b[1][1])
'''
#Looping X
#Slicing
'''
a = [10,20,30,40,50,60]
print(a[::])
print(a[:])
print(a[3:])
print(a[:5])
print(a[2:5])
print(a[1:5:2])
'''
#Methods
'''
#Index()
a = [10,20,30,20,50]
print(a.index(20))
print(a.index(30))
#count()
a = [10,20,30,20,50]
print(a.count(20))
print(a.count(30))
#Copy()
#shallow
x = [10,20,30]
y = x
print(x)
print(y)
y[1] = 200
print(x)
print(y)
#Deep
a = [10,20,30,40]
b = a.copy()
print(a)
print(b)
b[2] = 300
print(a)
print(b)
'''
#Insertion
'''
#append()
#Helps to add element at end
a = [10,20,30,40]
print(a)
a.append(50)
print(a)
a.append([100,200,300])
print(a)
#Extend()
a = [10,20,30,40]
print(a)
a.extend([50,60,70])
print(a)
#Insert()
a = [10,20,30,40]
print(a)
a.insert(0,5)
print(a)
a.insert(3,25)
print(a)
'''
#Deletion
'''
#remove()
a = [10,20,30,40,20]
print(a)
a.remove(20)
print(a)
#pop()
a = [10,20,30,40,50]
print(a)
a.pop()
print(a)
a.pop(2)
print(a)
#clear()
a = [100,200,300]
print(a)
a.clear()
print(a)
'''
#Updation
'''
#Indexing
a = [10,20,30,40]
print(a)
a[2] = 350
print(a)
#sort()
a = [45,2,98,1]
print(a)
a.sort()
print(a)
#reverse()
a = [45,2,98,1]
print(a)
a.reverse()
print(a)
'''
#Program - 1
'''
a = [40,12,23,1]
print(a)
a.sort()
print(a)
a.reverse()
print(a)
'''
#Program - 2
'''
a = [10,20,30,40]
print(a)
a.reverse()
print(a)
'''
#Built-in Functions
a = [1,2,3,4]
y = [0,0,0,1]
print(sum(a))
print(min(a))
print(max(a))
print(all(a))
print(all(y))
print(any(a))
print(any(y))
print(len(a))


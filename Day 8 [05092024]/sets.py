#Sets
#Creation
#Homogeneous
'''
s1 = {1,2,3,4}
print(s1)
print(type(s1))
s2 = set()
print(s2)
print(type(s2))
s3 = set([1,2,3,2,45,6])
print(s3)
print(type(s3))
'''
#Hetrogeneous X
#Accessing
#Looping X
#Methods
#union()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.union(s2))
print(s2.union(s1))
print(s1 | s2)
'''
#intersection()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.intersection(s2))
print(s2.intersection(s1))
print(s1 & s2)
'''
#difference()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1 - s2)
print(s2 - s1)
'''
#symmetric_difference()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
print(s1 ^ s2)
print(s2 ^ s1)
'''
#isdisjoint()
'''
s1 = {1,2,3,4}
s2 = {5,6}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))
'''
#issubset()
'''
s1 = {1,2,3,4}
s2 = {3,4}
print(s1.issubset(s2))
print(s2.issubset(s1))
'''
#issuperset()
'''
s1 = {1,2,3,4}
s2 = {3,4}
print(s1.issuperset(s2))
print(s2.issuperset(s1))
'''
#insertion
#methods()
#update()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s1.update(s2)
print(s1)
print(s2)
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s2.update(s1)
print(s2)
print(s1)
'''
#add()
'''
s1 = {1,2,3,4}
print(s1)
s1.add(4)
print(s1)
s1.add(7)
print(s1)
'''
#copy()
'''
s1 = {1,2,3,4}
s2 = s1.copy()
print(s2)
'''
#Deletion
#Del keyword
'''
s1 = {1,2,3,4}
print(s1)
del s1
print(s1)
'''
#methods
#remove()
'''
s1 = {1,2,3,4}
print(s1)
s1.remove(3)
print(s1)
s1.remove(30)
'''
#clear()
'''
s1 = {1,2,3,4}
print(s1)
s1.clear()
print(s1)
'''
#pop()
'''
s1 = {1,2,3,4}
print(s1)
s1.pop()
print(s1)
'''
#discard()
'''
s1 = {1,2,3,4}
print(s1)
s1.discard(3)
print(s1)
s1.discard(30)
print(s1)
'''
#Updation
#methods()
#update()
'''
s1 = {1,2,3,4}
print(s1)
s1.update({3,4,5,6})
print(s1)
'''
#intersection_update()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s1.intersection_update(s2)
print(s1)
print(s2)
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s2.intersection_update(s1)
print(s1)
print(s2)
'''
#difference_update()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s1.difference_update(s2)
print(s1)
print(s2)
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s2.difference_update(s1)
print(s1)
print(s2)
'''
#symmetric_difference_update()
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s1.symmetric_difference_update(s2)
print(s1)
print(s2)
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1)
print(s2)
s2.symmetric_difference_update(s1)
print(s1)
print(s2)
'''
#Frozensets
#Creation
#Homogeneous
'''
s1 = frozenset()
print(s1)
print(type(s1))
s2 = frozenset([1,2,3,4,2,3])
print(s2)
print(type(s2))
'''
#Hetrogeneous X
#Accessing
'''
#copy()
#union()
#intersection()
#difference()
#symmetric_difference()
#isdisjoint()
#issubset()
#issuperset()
'''
















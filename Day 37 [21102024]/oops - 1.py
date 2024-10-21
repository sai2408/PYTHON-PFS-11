#Syntax of class & object
'''
class class_name:
    constructors
    attributes
    methods

objectname = classname(values)
'''
#Problem - 1
'''
class sample1:
    a = 10
    b = 20
    def xyz(self):
        print("hello")
ob1 = sample1()
print(ob1.a)
print(ob1.b)
ob1.xyz()
ob2 = sample1()
print(ob2.a)
'''
#Problem - 2
'''
class problem2:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def summ(self):
        print(self.x+self.y)
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
obj = problem2(a,b)
obj.summ()
'''
#Problem - 3
'''
class problem2:
    def summ(self,x,y):
        print(x+y)
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
obj = problem2()
obj.summ(a,b)
'''






















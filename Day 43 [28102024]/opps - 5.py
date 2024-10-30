#Abstraction
'''
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def hello(self):
        print("I am hello from shape")
class rectangle(shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print(self.l * self.b)
class square(shape):
    def __init__(self,a):
        self.a = a
    def area(self):
        print(self.a * self.a)
r1 = rectangle(2,5)
r1.area()
s1 = square(3)
s1.area()
r1.hello()
s1.hello()
'''
#Exception Handling
#Program - 1
'''
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
'''
#Problem - 2
'''
try:
    a = int(input())
    b = int(input())
    c = a/b
except:
    print("Error Occurred")
else:
    print(c)
finally:
    print("Finally block")
'''
#Problem - 3
'''
try:
    a = int(input())
    b = int(input())
    c = a/b
except ZeroDivisionError:
    print("division error occured")
except:
    print("Another eooro occured")
else:
    print(c)
finally:
    print("Finally block")
'''
#Problem - 4
'''
try:
    a = int(input())
    b = int(input())
    c = a/b
except ZeroDivisionError:
    print("division error occured")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("Finally block")
'''

















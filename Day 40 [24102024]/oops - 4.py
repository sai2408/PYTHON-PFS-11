#Single Inheritance
#Problem - 1
'''
class parent:
    def hello(self):
        print("Hello from Parent class")
class child(parent):
    def bye(self):
        print("Bye from child")
c1 = child()
c1.bye()
c1.hello()
'''
#Problem - 2
'''
class base:
    def hello(self):
        print("Hello from base class")
class derived(base):
    def __init__(self):
        print("I am derived class constructor")
    def bye(self):
        print("Bye from derived class")
d1 = derived()
'''
#Problem - 3
'''
class base:
    def __init__(self):
        print("I am base class constructor")
    def hello(self):
        print("Hello from base class")
class derived(base):
    def bye(self):
        print("Bye from derived class")
d1 = derived()
'''
#Problem - 4
'''
class base:
    def __init__(self):
        print("I am base class constructor")
    def hello(self):
        print("Hello from base class")
class derived(base):
    def __init__(self):
        print("I am derived class constructor")
    def bye(self):
        print("Bye from derived class")
d1 = derived()
'''
#Multiple Inheritance
#Problem - 1
'''
class base1:
    def hello1(self):
        print("Hello from base1")
class base2:
    def hello2(self):
        print("Hello from base2")
class child(base1,base2):
    def hello3(self):
        print("Hello from base3")
ch = child()
ch.hello3()
ch.hello2()
ch.hello1()
'''
#Problem - 2
'''
class base1:
    def hello(self):
        print("Hello from base1")
class base2:
    def hello(self):
        print("Hello from base2")
class child(base2,base1):
    def hello1(self):
        print("Hello from base3")
ch = child()
ch.hello()
'''





















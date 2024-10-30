#Problem - 1 [ Theory ]
#Problem - 2 [ Theory ]
#Problem - 3
#Approach - 1
'''
class sample:
    def __init__(self):
        print("abc")
class child(sample):
    def __init__(self):
        super().__init__()
c = child()
'''
#Approach - 2
'''
class sample:
    def hello(self):
        print("abc")
class child(sample):
    def hello(self):
        super().hello()
c = child()
c.hello()
'''
#Problem - 4
'''
class sample:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        x = self.a+self.b
        return x
    def subtraction(self):
        x = self.a - self.b
        return x
    def multiplication(self):
        x = self.a * self.b
        return x
s = sample(10,5)
print(s.addition())
print(s.subtraction())
print(s.multiplication())
'''
#Problem - 5 [ 2M ]
'''
class abc:
    def __init__(self,a):
        self.a = a
    def factorial(self):
        x = 1
        for i in range(1,self.a+1):
            x = x * i
        print(x)
    def prime_number(self):
        x = True
        for i in range(2,self.a):
            if self.a%i == 0:
                x = False
                break
        if x == True:
            print("Prime Number")
        else:
            print("not a prime")
x = abc(12)
x.factorial()
x.prime_number()
'''
#Problem - 6 [ 2 M ]
'''
class dob:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
class details(dob):
    def __init__(self,name,day,month,year):
        self.name = name
        super().__init__(day,month,year)
    def display(self):
        print(f"Name: {self.name}")
        print(f"Date: {self.day}")
        print(f"Month: {self.month}")
        print(f"Year: {self.year}")
d = details("sai",24,8,2024)
d.display()
'''
#Problem - 7 [ 2 M ]
'''
class college:
    name = "SV"
    location = "TPT"
class cse(college):
    def __init__(self,sid,sname):
        self.sid = sid
        self.sname = sname
    def display(self):
        print(f"Name: {self.sname}")
        print(f"Id: {self.sid}")
        print(f"College Name: {self.name}")
        print(f"College Location: {self.location}")
class aiml(college):
    def __init__(self,sid,sname):
        self.sid = sid
        self.sname = sname
    def display(self):
        print(f"Name: {self.sname}")
        print(f"Id: {self.sid}")
        print(f"College Name: {self.name}")
        print(f"College Location: {self.location}")
cse1 = cse(101,"sai")
cse1.display()
aiml1 = aiml(201,"vardhan")
aiml1.display()
'''
#Problem - 8
'''
class public:
    sal = 15000
    exp = 6
    def __init__(self,name):
        self.name = name
    def display1(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.sal}")
        print(f"Experience: {self.exp}")
class private:
    snapid = "iamsai2408"
    instaid = "iamsai2408"
    def __init__(self,name):
        self.name = name
    def display2(self):
        print(f"Name : {self.name}")
        print(f"Snap id : {self.snapid}")
        print(f"Insta id: {self.instaid}")
class employee(private,public):
    def __init__(self,name):
        super().__init__(name)
e1 = employee("sai")
e1.display2()
e1.display1()
'''
#Problem - 9
'''
class vehicle:
    def __init__(self,model):
        self.model = model
    def display1(self):
        print(f"Model = {self.model}")
class car(vehicle):
    def __init__(self,mtype,model):
        self.mtype = mtype
        super().__init__(model)
    def display2(self):
        print(f"Motor type: {self.mtype}")
class motor(car):
    def __init__(self,name,mtype,model):
        self.name = name
        super().__init__(mtype,model)
    def display3(self):
        print(f"Name: {self.name}")
m1 = motor("alto","maruthi",2019)
m1.display3()
m1.display2()
m1.display1()
'''
        





























































    










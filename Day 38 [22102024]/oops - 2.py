#Problems on oops
'''
1. Create a class Rectangle that has attributes length and width.
Add methods to calculate and return the area and perimeter of the
rectangle. Create a constructor to initialize the attributes.
2. Write a Python program using classes to represent a Student and
store details such as name, roll_number, marks in different subjects.
Implement a method to calculate the average marks and display the
student’s grade based on that average.
3. Create a Python class BankAccount with the following methods:
    __init__ to initialize account balance.
    deposit to add money to the account.
    withdraw to withdraw money from the account.
    get_balance to display the current balance.
Instantiate the class and simulate a few deposits and withdrawals.
4. Create a class Employee with attributes like name, age, and salary.
Write methods to give a raise in salary and display the employee’s
details. Add a method to check if the employee is eligible for
retirement (consider 60 years as the retirement age).
5. Define a class Book that represents a book in a library. The class
should have attributes like title, author, year, and availability.
Implement methods to borrow and return a book. Maintain the
availability status of each book using a class variable.
'''
#Problem - 1
'''
1. Create a class Rectangle that has attributes length and width.
Add methods to calculate and return the area and perimeter of the
rectangle. Create a constructor to initialize the attributes.
'''
#Program
'''
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        x = self.length * self.width
        return x
    def perimeter(self):
        x = 2 * (self.length + self.width )
        return x
r1 = Rectangle(2,5)
r2 = Rectangle(10,40)
print(r1.area())
print(r1.perimeter())
print(r2.area())
print(r2.perimeter())
'''
#Problem - 2
'''
2. Write a Python program using classes to represent a Student and
store details such as name, roll_number, marks in different subjects.
Implement a method to calculate the average marks and display the
student’s grade based on that average.
'''
#Program
'''
class Student:
    def __init__(self,name,roll,english,maths,science):
        self.name = name
        self.roll = roll
        self.english = english
        self.maths = maths
        self.science = science
    def result(self):
        avg = (self.english + self.maths + self.science)//3
        grade = ""
        if avg >= 70:
            grade = "A+"
        elif avg >= 50:
            grade = "A"
        else:
            grade = "B"
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll}")
        print(f"Grade: {grade}")
name = input("Enter Student Name: ")
roll = int(input("Enter Roll Number: "))
english = int(input("Enter Marks in English: "))
maths = int(input("Enter Marks in Maths: "))
science = int(input("Enter Marks in science: "))
s1 = Student(name,roll,english,maths,science)       
s1.result()
'''
#Problem - 3
'''
3. Create a Python class BankAccount with the following methods:
    __init__ to initialize account balance.
    deposit to add money to the account.
    withdraw to withdraw money from the account.
    get_balance to display the current balance.
Instantiate the class and simulate a few deposits and withdrawals.
'''
#Program
'''
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self,amount):
        if amount <= self.balance:
            print("Withdraw Sucessfull")
            self.balance = self.balance - amount
        else:
            print("Insufficient Balance")
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit Sucessfull")
    def get_balance(self):
        print(f"Balance: {self.balance}")
a1 = BankAccount(1000)
a1.get_balance()
a1.withdraw(2000)
a1.withdraw(500)
a1.get_balance()
a1.deposit(5000)
a1.get_balance()
'''
#Problem - 4
'''
4. Create a class Employee with attributes like name, age, and salary.
Write methods to give a raise in salary and display the employee’s
details. Add a method to check if the employee is eligible for
retirement (consider 60 years as the retirement age).
'''
#Program
'''
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def raise_salary(self,amount):
        self.salary = amount
    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
    def check(self):
        if self.age >= 60:
            print("Eligible For Retierement")
        else:
            print("Not Eligible for Retierement")
e1 = Employee("Sai",70,1300000)
e1.details()
e1.raise_salary(1500000)
e1.details()
e1.check()
e2 =Employee("venkat",34,1000000)
e2.details()
e2.raise_salary(1500000)
e2.details()
e2.check()
'''
#Problem - 5
class dateofbirth:
    def __init__(self,date,month,year):
        self.date = date
        self.month = month
        self.year = year
    def details1(self):
        print(f"DOB: {self.date}-{self.month}-{self.year}")
class student:
    def __init__(self,name,branch,date,month,year):
        self.name = name
        self.branch = branch
        self.dob = dateofbirth(date,month,year)
    def details(self):
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")
        self.dob.details1()
s1 = student("sai","CSE",24,8,2024)
s1.details()






    


















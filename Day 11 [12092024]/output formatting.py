#Explanation
'''
#Input Formatting
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
height = float(input("Enter Your Height: "))
#Output format:
{name} is {age} years old. Height is {height}
#Output Formatting
#Normal Method
print(name,"is",age,"years old. Height is",height)
#Modulo Operator
print("%s is %d years old. Height is %f"%(name,age,height))
#F-format
print(f"{name} is {age} years old. Height is {height}")
#dot format
print("{} is {} years old. Height is {:.3f}".format(name,age,height))
'''
#Problem - 1
'''
#Input:
Sai,vardhan
24-8-2000
5.76
#Ouput:
First name: Sai
Last name: vardhan
Height: 5.760
Date of Birth Details:
Date : 24
Month : August
Year : 2000
#Program
d = {1:"Jan",2:"Feb",3:"Mar",4:"April",5:"May",6:"June",7:"July",8:"August",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
fn,ln = input().split(",")
dd,mm,yy = map(int,input().split("-"))
height = float(input())
print("First name: {}".format(fn))
print("Last name: {}".format(ln))
print("Height : {:.3f}".format(height))
print("Date of Birth Details:")
print("Date : {}".format(dd))
print("Month : {}".format(d[mm]))
print("Year : {}".format(yy))
'''






















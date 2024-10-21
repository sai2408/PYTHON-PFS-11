#Problem - 1
#Approach - 1
'''
f1 = open("hello.txt","r")
print(f.read())
f1.close()
'''
#Approach - 2
'''
f1 = open("hello.txt","r")
x = f.read()
print(x)
f1.close()
'''
#Problem - 2
#Approach - 1
'''
f = open("test.txt","w")
f.write("Hello world\nhello codegnan")
f.close()
'''
#Appraoch - 2
'''
f = open("test.txt","w")
f.write("Hello world\n")
f.write("hello codegnan")
f.close()
'''
#Problem - 3
#Approach - 1
'''
from os import *
mkdir("abc")
chdir("xyz")
print(listdir())
'''
#Appraoch - 2
'''
from os import *
mkdir("abc")
chdir("xyz")
x = listdir()
print(x)
'''
#Approach - 3
'''
from os import *
mkdir("abc")
chdir("xyz")
x = listdir()
for i in x:
    print(i)
'''
#Problem - 4
#Appraoch - 1
'''
import re
pattern = r'\s'
text = "hello codegnan, how are you"
matches = re.findall(pattern,text)
print(len(matches))
'''
#Approach - 2
'''
import re
pattern = re.compile(r'\s')
text = "hello codegnan, how are you"
matches = re.findall(pattern,text)
print(len(matches))
'''
#Problem - 5
#Approach - 1
'''
import re
pattern = r'\W'
text = "Hello codegnan, how are you"
matches = re.findall(pattern,text)
print(matches)
'''
#Appraoch - 2
'''
import re
pattern = re.compile(r'\W')
text = "Hello codegnan, how are you"
matches = re.findall(pattern,text)
print(matches)
'''
#Problem - 6
#Approach - 1
'''
import re
pattern = r'\bhello\b'
text = "Hello Sai, hello codegnan"
matches = re.findall(pattern,text)
print(len(matches))
'''
#Appraoch - 2
'''
import re
pattern = re.compile(r'\bhello\b')
text = "Hello Sai, hello codegnan"
matches = re.findall(pattern,text)
print(len(matches))
'''
#Approach - 3
'''
import re
pattern = r'hello'
text = "Hello Sai, hello codegnan"
matches = re.findall(pattern,text)
print(len(matches))
'''
#Approach - 4
'''
import re
pattern = re.compile(r'hello')
text = "Hello Sai, hello codegnan"
matches = re.findall(pattern,text)
print(len(matches))
'''
#Problem - 7
'''
import re
pattern = r'^hello'
text = "  hello world"
matches = re.findall(pattern,text)
if len(matches) == 0:
    print("Not starting with hello")
else:
    print("starting with hello")
'''
#Problem - 8
'''
import re
pattern = re.compile(r'ab{3}')
text = "abbb ab, baba,abb,"
matches = re.search(pattern,text)
print()
'''
#Problem - 9
'''
import re
pattern = r'\d{7}-\d{4}'
text = "7893566-0611"
matches = re.findall(pattern,text)
print(matches)
'''
#Problem - 10
'''
import re
p1 = r'.+@gmail.com'
p2 = r'\d{2}-\d{2}/\d{4}'
gmail =input()
dob = input()
gmailmatch = re.findall(p1,gmail)
dobmatch = re.findall(p2,dob)
if len(gmailmatch) == 0:
    print("gmail not matches")
else:
    print("gmail matched")
if len(dobmatch) == 0:
    print("dob not matched")
else:
    print("dob matched")
'''
































#Strings
#Creation
#Homogeneous
'''
a = "hello World"
print(a)
print(type(a))
b = 'hello World'
print(b)
print(type(b))
'''
#Heterogeneous
#Accessing
#Indexing
'''
s = "Sai Vardhan"
#+ve
print(s[4])
#-ve
print(s[-1])
print(s[-7])
'''
#Looping
#slicing
'''
s = "abcdefghijklm"
#+ ve
print(s[::])
print(s[::1])
print(s[:])
print(s[::2])
print(s[1::2])
print(s[3:8:2])
#- ve
'''
#methods
'''
s = "abcdefgh"
'''
#startswith()
'''
print(s.startswith("a"))
print(s.startswith("abc"))
print(s.startswith("abcdefgh"))
print(s.startswith("xyz"))
print(s.startswith("bc"))
'''
#endswith()
'''
print(s.endswith("h"))
print(s.endswith("gh"))
print(s.endswith("abcdefgh"))
print(s.endswith("a"))
'''
#isdigit()
'''
s1 = "123"
print(s.isdigit())
print(s1.isdigit())
'''
#isalpha()
'''
s1 = "123"
print(s.isalpha())
print(s1.isalpha())
'''
#isdecimal()
'''
s1 = "123"
print(s.isdecimal())
print(s1.isdecimal())
'''
#isalnum()
'''
s1 = "123"
s2 = "abc"
s3 = "123abc"
s4 = "123_abc"
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s4.isalnum())
'''
#istitle()
'''
s1 = "hello world"
print(s1.istitle())
s2 = "Hello World"
print(s2.istitle())
s3 = "Hello world"
print(s3.istitle())
'''
#find()
'''
s1 = "Sai Vardhan"
print(s1.find("a"))
#rfind()
print(s1.rfind("a"))
#count()
print(s1.count("a"))
'''
#functions
#len()
#max()
#min()
'''
s = "abcda"
print(len(s))
print(max(s))
print(min(s))
'''

#Reading the Data from a file
'''
f = open("hello1.txt","r")
print(f.read())
f.close()
'''
#Write the data into File
#Example - 1
'''
f2 = open("hello2.txt","w")
f2.write("Hey Guys")
f2.close()
'''
#Example - 2
'''
f3 = open("hello3.txt","w")
f3.write("This is new File")
f3.close()
'''
#Append
'''
f4 = open("hello4.txt","a")
f4.write(" Sai Vardhan")
f4.close()
'''
#Read and Write
'''
f5 = open("hello4.txt","r+")
f5.write("Hello Everyone")
f5.seek(0)
print(f5.read())
f5.close()
'''

















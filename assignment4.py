# Question4 :Write a Python program to count the number of lines in a text file

import io
fo=open("aditi.txt","w+")
fo.write("hello\nAditi\nChikshe\nZensar")
fo.close()
filename="aditi.txt"
myfile = open(filename)
lines= len(myfile.readlines())
print "There are%d lines in %s "%(lines,filename)


'''
output:

There are4 lines in aditi.txt
'''

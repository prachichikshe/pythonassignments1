# 8.Define a function max() that takes two numbers as arguments and returns the largest of them.
def max(a, b):
    #DocString
    """ Function to find out the maximum of two numbers """
    
    if a > b:
        return a
    else:
        return b

A=input('Enter the first number')

B=input('Enter the second number')

print (str(max(A,B)) + ' is larger')

#Output
#Enter the first number 56
#Enter the second number 89
#89 is larger

#9.Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
def max_of_three(a,b,c):
    #DocString
    
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print ("Function to find the largest of three numbers")
firstNumber=int(input("Enter the first  number"))
secondNumber=int(input("Enter the second  number"))
thirdNumber =int(input("Enter the third  number"))
print ("Largest of " +str(firstNumber) +", " +str(secondNumber) +", " +str(thirdNumber) +" is " +str(max_of_three(firstNumber,secondNumber,thirdNumber)))

#Output
#Enter the first  number4
#Enter the second  number7
#Enter the third  number9
#Largest of 4, 7, 9 is 9

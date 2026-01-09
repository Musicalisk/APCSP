# Write a program that accepts a number as input, and prints just the decimal portion.
# Your program should also work if a negative number is inputted by the user.
# Lastly, write a print statement that states “The final outcome is: ”, followed by the decimal portion, and remember to change the final outcome to a string.
import math
num1=math.fabs(float(input('Enter a number: ')))
num2=int(num1)
print('The final outcome is:',num1-num2)
# Write a program that takes three numbers as input from the user, and prints the smallest.
# Hint: Remember that the numbers should be compared numerically.
# Any input from the user must be transformed into an integer, but printed as a string.
num1=int(input('Enter a number: '))
num2=int(input('Enter a number: '))
num3=int(input('Enter a number: '))
print('Smallest:',str(min(num1,num2,num3)))
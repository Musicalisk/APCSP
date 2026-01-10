# Write a program to convert a fraction to a decimal. 
# Have your program ask for the numerator first, then the denominator. 
# Make sure to check if the denominator is zero. 
# If it is, print out "Cannot divide by zero."
# Hint: Since this lesson uses if-else statements, remember to use at least one if-else statement in each of your answers to receive full credit.
top=int(input('Enter the numerator: '))
bottom=int(input('Enter the denominator: '))
if bottom==0:print('Cannot divide by zero.')
else:print('Decimal:',top/bottom)
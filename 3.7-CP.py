# When we read code and predict its output, it is called tracing code.
# For this lesson, you will come up with your own challenging algorithm for other students to trace. 
# It must contain at least 4 if statements, 1 else statement and use at least one and or or boolean condition.
# Note: Elif statements will not count - your statements must be if statements. 
# Each if statement should use a unique variable name.
#For this challenge, try reading 3 or 4 of your classmates' code as well. 
# Trace their code and predict what it will output, then check the code by running it to see if you got it right, and submit your work for a grade.
from math import fabs
top=fabs(int(input('Enter Numerator: ')))
bottom=fabs(int(input('Enter Denominator: ')))
if bottom==0:print('Can\'t divide by Zero')
print('Decimal:',top/bottom)
if(top%bottom==0):print('Zero')
else:print('Not Zero')
if top==bottom:print('YOUR LAZY')
if top==1 or bottom==1:print('UNO!')
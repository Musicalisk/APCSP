# Write a program to input 6 numbers. 
# After each number is input, print the smallest of the numbers entered so far.
num1=float(input('Enter a number: '))
key=num1
print('Smallest:',key)
num2=float(input('Enter a number: '))
if num2<=key:key=num2
print('Smallest:',key)
num3=float(input('Enter a number: '))
if num3<=key:key=num3
print('Smallest:',key)
num4=float(input('Enter a number: '))
if num4<=key:key=num4
print('Smallest:',key)
num5=float(input('Enter a number: '))
if num5<=key:key=num5
print('Smallest:',key)
num6=float(input('Enter a number: '))
if num6<=key:key=num6
print('Smallest:',key)
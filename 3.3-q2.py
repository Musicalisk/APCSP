# Ask the user to enter a number for red, green, and blue components of an RGB value, which takes a certain amount of red, green, and blue colors and produces a new color.
# Test the numbers that are input by the user and check that each value is between 0 and 255 (inclusive).
# If a color's value is outside of this range, print which color's number is not correct (e.g., "Red number is not correct" if the red value is 300).
# Multiple colors may be out of range.
# The order of the colors should be the same as the sample runs below; red, then green, then blue.
# Hint: Since this lesson uses boolean operators, remember to use at least one boolean operator in each of your answers to receive full credit.
red=int(input('Enter the red: '))
green=int(input('Enter the green: '))
blue=int(input('Enter the blue: '))
if not red<=255 or red<0:print('Red number is not correct.')
if not green<=255 or green<0:print('Green number is not correct.')
if not blue<=255 or blue<0:print('Blue number is not correct.')
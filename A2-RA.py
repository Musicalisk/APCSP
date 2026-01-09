# https://files.projectstem.org/CSFundamentals/CSF_Images/U2_A2_Lab_image.png
# find the area of an irregularly shaped room with the shape as shown above.
# Ask the user to enter the values for sides A, B, C, D, and E and print out the total room area.
# Remember the formula for finding the area of a rectangle is length * width and the area of a right triangle is 0.5 * the base * height.
# Please note the final area should be in decimal format.
from math import fabs
sideA=fabs(float(input('Enter side A:')))
sideB=fabs(float(input('Enter side B:')))
sideC=fabs(float(input('Enter side C:')))
sideD=fabs(float(input('Enter side D:')))
sideE=fabs(float(input('Enter side E:')))
print('Room Area:',(sideA*sideB)+((sideA-sideC)*(sideD-sideB-sideE))+(0.5*((sideA-sideC)*sideE)))
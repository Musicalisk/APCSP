# Test if a date is a fee day for a subscription based on the day of the month (the subscription has fees on the 16th and the 29th every month).
from math import fabs
num1=fabs(int(input('Enter today\'s day numerically: ')))
if(num1>=32):print('Not a possible day.')
if not (num1 == 16 or num1 == 29):print('Sorry, not a fee day.')
else:print('It\'s a fee day!')
# Write a program that asks the user to enter a city name, and then prints Oh! CITY is a cool spot. 
# Your program should repeat these steps until the user inputs Nope.
city=input('Please enter a city name: (Nope to end) ')
while city!='Nope':
    print('Oh!',city,'is a cool spot.')
    city=input('Please enter a city name: (Nope to end) ')
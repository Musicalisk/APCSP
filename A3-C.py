# A chatbot is a computer program designed to emulate human conversation. 
# For this program, you will use if statements, user input, and random numbers to create a basic chatbot.
# The Scenario
# You have decided to design a fashion chatbot that helps people pick out their fashion preferences.
# Your bot can gauge what types of clothes and accessories the user might like.
# Your chatbot should ask the user the following (minimum requirements for the grader) and then give answers depending on the answers the user inputs:
# at least 6 questions
# at least 3 if-elif-else statements
# ​the use of the random module and randomly generated numbers
# Based on these criteria, some responses will be based on what the user types and some will be based on random numbers.
# For example, if the chatbot asks what is your favorite head accessory, your chatbot might respond 'I also think baseball hats are best.' in response to a user input of baseball hats, or 'I love beanies!' in response to a user input of beanies.
# Additionally, you could also have a random number generated between, say, 1 and 3 and have a corresponding response depending on the number to randomly answer with 'That’s in right now.' or 'Wow, so stylish!', and so on.
# Note that in order to pass all of the test cases, your randomly generated numbers should not be dependent on user input (for example, you would not want to include a situation where if the user inputs a specific phrase, then a random number is generated). 
# The randomly generated numbers should prompt a reply from the chatbot, and should do so separately from the user input statements that prompt a reply from the chatbot
from math import fabs
from random import randint
name=input('What is your Name?\n')
# Question 1 ^
age=fabs(int(input('\nHow old are you?\n')))
# Question 2 ^
q1=randint(1,3)
# random module 1 ^
if q1==1:print('I\'m',str(age),'too!')
elif q1==2:print('I\'m',str(age-1)+'.')
else:print('I\'m',str(age+1)+'.')
# if-elif-else statement 1 ^
band=input('\n'+name+', What is your favorite muscical band?\n')
# Question 3 ^
q2=randint(1,3)
# random module 2 ^
if q2==1:print(band,'is my favorite too!')
elif q2==2:print('My favorite band is Deftones.')
else:print('I like',band,'just as much as Pleymo, a French band!')
# if-elif-else statemnt 2 ^
booka=input('\nWhat is your favorite book?\n')
# Question 4 ^
bookb=input('\nDo you like it?\n')
# Question 5 ^
phone=input('\nWhat\'s your phone number?\n')
# Question 6 ^
q3=randint(1,3)
# random module 3 ^
if q3==1:print('Thanks, See you later!')
elif q3==2:print(phone,'? Alright, thanks!')
else:print('Mine is (123)-4567-890, call later?')
# if-elif-else statement 3 ^
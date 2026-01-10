# Input a grade level (Freshman, Sophomore, Junior, or Senior) and print the corresponding grade number [9-12]. 
# If it is not one of those grade levels, print Not in High School.
# Hint: Since this lesson uses else-if statements, remember to use at least one else-if statement in your answer to receive full credit.
grade=input('What year of high school are you in? ')
if grade=='Freshman':print('You are in grade: 9')
elif grade=='Sophomore':print('You are in grade: 10')
elif grade=='Junior':print('You are in grade: 11')
elif grade=='Senior':print('You are in grade: 12')
else:print('Not in High School')
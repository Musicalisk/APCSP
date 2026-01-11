# Write a loop that continually asks the user what pets the user has until the user enters stop, in which case the loop ends. 
# It should acknowledge the user in the following format. 
# For the first pet, it should say 'You have one cat. Total # of Pets: 1 ' if they enter 'cat', and so on.
key=0
count=0
while key!='stop':
    key=input('What pet do you have? ')
    if key=='stop':print('')
    else:   
        count+=1
        print('You have one',key+'. Total # of Pets:',count)
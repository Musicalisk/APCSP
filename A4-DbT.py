from math import fabs
user=input('How many numbers do you need to check? ')
cDiv=0
cIndiv=0
for i in range(0, int(user), 1):
    num=int(input('Enter number: '))
    if(num%3==0):
        print(num,'is divisible by 3.')
        cDiv+=1
    else:
        print(num,'is not divisible by 3.')
        cIndiv+=1
print('You entered',cDiv,'number(s) that are divisible by 3.')
print('You entered',cIndiv,'number(s) that are not divisible by 3.')
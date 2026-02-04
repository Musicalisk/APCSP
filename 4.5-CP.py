num=0
user=''
while user!='DONE':
    user=input('Please enter the next word: ')
    if user=='DONE':
        print('A total of',num,'words were entered.')
    else:
        num+=1
        print('#'+str(num)+': You entered the word',user)
# Write a program that inputs numbers and keeps a running sum. 
# When the sum is greater than 200, output the sum as well as the count of how many numbers were entered.
sum=0
count=0
while sum<=200:
    num=float(input('Enter a number: '))
    sum+=num
    count+=1
print('\nSum:',sum,'\nNumbers Entered:',count)
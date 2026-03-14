def leap_year(y):
    if (y%4==0 and y%100!=0)or(y%400==0):return 1
    else:return 0
def number_of_days(m,y):
    if m in [4,6,9,11]:return 30
    elif m in [1,3,5,7,8,10,12]:return 31
    else:
        l=leap_year(y)
        if l==0:return 28
        else:return 29
def days_passed(d,m,y):
    l=leap_year(y)
    s=0
    if l==0:
        for i in range((m-1)):
            s+=number_of_days((i+1),y)
        return 364-(s+d)
    else:        
        for i in range((m-1)):
            s+=number_of_days((i+1),y)
        return 365-(s+d)
def menus_handler(i,d,m,y):
    if i==1:
        if (m<1)or(m>12):return 'Not a valid input!'
        else:return number_of_days(m,y)
    elif i==2:
        if (m<1)or(m>12):
            if (d<1)or(d>31):return 'Not a valid input!'
            else:return days_passed(d,m,y)
        else:return 'Not a valid input!'
    else:return 'Not a valid input!'
print('Please enter a date')
day=int(input('Day: '))
month=int(input('Month: '))
year=int(input('Year: '))
menu=int(input('Menu:\n1) Calculate the number of days in the given month.\n2) Calculate the number of days passed in the given year.\n'))
print(menus_handler(menu,day,month,year))
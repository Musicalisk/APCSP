def Get_Winnings(m,s):
    if m.isnumeric()==True:
        if m == '1':
            c=75000+s
            return c
        if m == '2':
            c=150000+s
            return c
        if m == '3':
            c=225000+s
            return c
        if m == '4':
            c=300000+s
            return c
        if m == '5':
            c=375000+s
            return c
        else:
            c='Invalid'
            return c
    else:
        c='Invalid'
        return c
def Average_Winnings(m,c):
    d=int(m)
    avr=c/d
    return avr
medals=input("Enter Gold Medals Won: ")
sponsor=int(input('For how many dollars was your event sponsored?: '))
cash=Get_Winnings(medals,sponsor)
average=Average_Winnings(medals,cash)
print("Your prize money is:",cash)
print('Your average award money per gold medal was',average)
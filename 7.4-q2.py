def Get_Winnings(m,s):
    if m.isnumeric()==True:
        if m == '1':
            cash=75000+s
            return cash
        if m == '2':
            cash=150000+s
            return cash
        if m == '3':
            cash=225000+s
            return cash
        if m == '4':
            cash=300000+s
            return cash
        if m == '5':
            cash=375000+s
            return cash
        else:
            cash='Invalid'
            return cash
    else:
        cash='Invalid'
        return cash
medals=input("Enter Gold Medals Won: ")
sponsor=int(input('For how many dollars was your event sponsored?: '))
cash=Get_Winnings(medals,sponsor)
print("Your prize money is:",cash)
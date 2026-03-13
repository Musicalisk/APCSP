def Get_Winnings(m):
    if m.isnumeric()==True:
        if m == '1':
            cash=75000
            return cash
        if m == '2':
            cash=150000
            return cash
        if m == '3':
            cash=225000
            return cash
        if m == '4':
            cash=300000
            return cash
        if m == '5':
            cash=375000
            return cash
        else:
            cash='Invalid'
            return cash
    else:
        cash='Invalid'
        return cash
medals=input("Enter Gold Medals Won: ")
cash=Get_Winnings(medals)
print("Your prize money is:",cash)
yard1=int(input('Enter Yards: '))
feet1=int(input('Enter Feets: '))
yard2=int(input('Enter Yards: '))
feet2=int(input('Enter Feets: '))
total1=(yard1*3)+feet1
total2=(yard2*3)+feet2
final=(total1+total2)
print('Yards:',final//3,'Feet:',final%3)
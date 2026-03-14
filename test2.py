def words(w, n):
  if(n > 5):
    return w.upper()
  else:
    return w.lower()
def mystery(a = 2, b = 1, c = 3):
    return 2 * a + b + 3 * c
def leap_year(y):
    if (y%4==0 and y%100!=0)or(y%400==0):
        return 1
x=4
y=3
z=7
print(mystery(x,y,z))
x=5
y=8
print(mystery(x,y))
x=1
print(mystery(x))
print(mystery())
print(words('wOrd',0))
print(words('wOrd',10))
print(leap_year(2020))
print(leap_year(2021))
print(leap_year(2120))
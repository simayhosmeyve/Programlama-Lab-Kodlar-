from sympy import Symbol
from sympy import factor,expand
from sympy import pprint
x = Symbol('x') #x'i sembol olarak aldık
y = Symbol('y')

#Örnekler
#p = x*(x+x)
#p = (x+2)*(x+3)
expr1 = x**2 - y**2
factor(expr1)
#sonuc=(x+y)^(x-y)  carpanlara ayırır
factors1 = factor(expr1)
expand(factors1)
#sonuc= x**2 - y**2 açılıma karsılık gelen formülü yazar,sadelestirir
expr2 = x**3+3*x**2*y+3*x*y**2+y**3
pprint(expr2) #Yazımı düzenliyor 
pprint(factor(expr2))

series = x
n=5
x_value=10
for i in range(2,n+1):
    series = series + (x**i)/i
    series_value = series.subs({x:x_value})
pprint(series)
print(series_value)

expr = x*x + x*y + x*y + y*y
d = expr.subs({x:1, y:2}) 
#subs() sembolleri ve değerleri içeren dictionary oluşturur
d2 = expr.subs({x:1-y}) #x yerine 1-y koyduk
print(d)
print(d2)


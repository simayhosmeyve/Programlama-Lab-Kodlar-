#Limit fonksiyonu ile türev bulma 
from sympy import Symbol, Limit 
t = Symbol('t') 
t1 = Symbol('t1')
delta_t = Symbol('delta_t')
St = 5*t**2 + 2*t + 8

St1 = St.subs({t: t1}) #St fonksiyonunda t yerine t1 koyduk
St1_delta = St.subs({t: t1 + delta_t})

Limit((St1_delta-St1)/delta_t, delta_t, 0).doit() 
#delta_t'ye göre türevini alır
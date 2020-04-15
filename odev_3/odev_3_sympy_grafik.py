#BİNOM DAGILIMI

import sympy as sym
from sympy import *
import matplotlib.pyplot as plt

n = Symbol('n')#Yapılan deney sayısı
x = Symbol('x')#İstenen basarı sayısı
p = Symbol('p')#Basarma ihtimali
q = Symbol('q')#Basaramama ihtimali q=(1-p)

def factorial(sayi):
      if sayi==0:
        return 1
      else:
        fact = 1
        while(sayi > 1): 
            fact *= sayi 
            sayi-= 1
      return fact

#kombinasyon=factorial(n)/(factorial(n-x)*factorial(x)) 
#Seklinde de hesaplanabilir
kombinasyon=sym.binomial(n,x)
olasılık=(p**x)*(q**(n-x))
binom_dagılımı = kombinasyon*olasılık#binom dagılımı hesaplaması

pprint(binom_dagılımı)

n_values=[]
x_values=[]
for value in range(0,100):#n=100 deney sayısı
    a = binom_dagılımı.subs({p:0.6,q:0.4,n:value,x:30}).evalf()
    #basarı olasılıgı yüzde 60
    #x=30 istenen basarı sayısı
    n_values.append(value)
    x_values.append(a)

plt.plot(n_values,x_values) 
plt.show()

#Binom dagılımı n tane deney icinden x tane basarılı deney cıkmasını basarı olasılıgına bakarak hesaplar
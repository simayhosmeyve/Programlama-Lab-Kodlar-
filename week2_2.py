from sympy import sym
from sympy import Symbol
from sympy import pprint
import matplotlib.pyplot as plt
import sympy.plotting as syp


sigma = Symbol('sigma') #Matematiksel sembol belirttik
mu = Symbol('mu')
x = Symbol('x')
pprint(2*sym.pi*sigma)#Sembollerle yazar
pprint(sym.sqrt(2*sym.pi*sigma))#sqrt() ile karekök aldık

part_1 =1/(sym.sqrt(2*sym.pi*sigma**2))
part_2=sym.exp(-1*((x-mu)**2)/(2*sigma**2))

gauss_function = part_1*part_2
pprint(gauss_function)

syp.plot(gauss_function.subs({mu:1,sigma:3}),(x,-10,10),title='Gauss dagılımı')#Grafik çizme
#mu ve sigmaya deger atadık.İki bilinmeyen kaldı(x,y)
#Grafik -10 ve 10 arasında çizilir

#Döngü ile olusturma
x_values=[]
y_values=[]
for value in range(-10,10):
    y = gauss_function.subs({mu:1,sigma:3,x:value}).evalf() 
    #evalf() sayısal degerlere donusturuyor
    x_values.append(value)
    y_values.append(y)

plt.plot(x_values,y_values) # grafikte x değerleri için hangi y değerlerine karşılık geldiğini atıyoruz
plt.show()  # grafiği console da gösteriyoruz
# syp.plot(gauss_function.subs({mu:1,sigma:3}),(x,-10,10),title='Gauss')
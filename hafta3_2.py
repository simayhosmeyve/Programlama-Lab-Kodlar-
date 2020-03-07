#Olasılık
#İstenilen durum/Tüm durumlar
def probability(space,event):
    return len(event)/len(space)

def checkPrime(number):
    if number!=1:
        for factor in range(2,number):
            if  number%factor==0:
                return False
    else:
        return False
    return True

from sympy import FiniteSet

space = FiniteSet(*range(1,21)) #Virgülle ayrılmış elemanlar oluşturuluyor
primes=[]
for number in space:
    if checkPrimePrime(number)==True:
            primes.append(number)

p = probability(space,event)
print(p)

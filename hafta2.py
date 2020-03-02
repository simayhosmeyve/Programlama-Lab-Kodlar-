
#Insertion Sort
#Listede bir kısım sıralı kısım olarak ayrılıyor ve ekleme yaparak sıralı kısımda karşılaştırma yapıyor
def insertionSort(liste):
    n = len(liste)
    for i in range(1,n):
        key = liste[i]
        j = i-1
        while j>=0 and key<liste[j]:    
            j=j-1
            liste[j+1]=liste[j]
            liste[j+1]=key
liste = [3,10,2,6,5,9]
insertionSort(liste)
print(liste)

#Shell Sort
#Atlama yaparak ve atlama sayısını yarıya indirerek sıralar
def shellSort(liste):
    n=len(liste)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = liste[i]
            j = i
            while j >= gap and liste[j - gap] > temp:
                liste[j] = liste[j - gap]
                j = j-gap
        liste[j] = temp
        gap //= 2
liste = [3,10,2,6,5,9]
shellSort(liste,len(liste))
print(liste)


import sys
import csv

aylar=[]
degerler=[] #Ayların histogramından aldığımız sonuçlar


with open(sys.argv[1]+'\input_hw_2.csv','r',encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_file:
        aylar.append(int(line.split(";")[3].split("-")[1]))

aylar=sorted(aylar)
def histogram(aylar):
    Dic=dict()
    for item in aylar:
        if item in Dic:
            Dic[item]=Dic[item]+1
        else:
            Dic[item]=1
    return Dic


h=histogram(aylar)
items = h.items() 
for item in items: 
    degerler.append(item[1]) 
   
def ortalama(degerler):
    toplam=0
    for i in degerler:
        toplam+=i
    return int(toplam/len(degerler))

degerler= sorted(degerler)
def medyan(degerler):
    n=len(degerler)
    if n%2==1:
        ortanca = int((n/2)+1)
        return degerler[ortanca-1]

    else:
        ortanca1=int((n/2)-1)
        ortanca2=ortanca1+1
        return (degerler[ortanca1]+degerler[ortanca2])/2



file = open(sys.argv[2]+'\180401017_hw_2_output.txt', 'w', encoding="utf-8")
file.write("Ortalama:")
file.write(str(ortalama(degerler)))
file.write("\nMedyan:")
file.write(str(medyan(degerler)))
file.close()


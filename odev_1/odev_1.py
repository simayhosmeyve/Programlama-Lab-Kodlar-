histogramList = []
def histogram(histogramList):
    myDic = dict()
    for i in histogramList:
        if i in myDic:
            myDic[i] += 1
        else:
            myDic[i] = 1
    return myDic

def frekans(myDic):
    kelimeFrekans, key = 0, ""
    for i in myDic:
        if myDic[i] > kelimeFrekans:
            key = i
            kelimeFrekans = myDic[i]
    return key

text = []
def readFile(text):
    dosya = open("1.txt", "r")
    for i in dosya:
        for j in i.split():
            text.append(j.lower())
    for i in dosya:
        if (i != "\n"):
            i = i.replace("\n", "")
            text.append(i)


def writeInput():
    file = open("input.txt", "w")
    while (1):
        inp = input("Metin giriniz : ")
        if (inp == "-1"):
            break
        if len(inp.split()) > 5:
            print("5ten fazla kelime giremezsiniz")
            break
        file.write(inp)
        file.write("\n")
    file.close()


def readInput():

    dosya = open("input.txt", "r")
    for satir in dosya:
        arananlar.clear()
        for i in satir.split():
            arananlar.append(i)
        kelimeOnerme(arananlar)

maxKelimeler = []
def writeOutput(maxKelimeler):
    dosya = open("output.txt","w")
    uzunluk = len(maxKelimeler)
    i=0
    while i<uzunluk:
        dosya.write(maxKelimeler[i])
        dosya.write("\n")
        i=i+1
    dosya.close()

def kontrol(text):
    for i in range(0,len(text)):
        text[i] = text[i].replace(',','')
        text[i] = text[i].replace('.','')

def kelimeOner(myDic, kelimeFrekans):
        if len(myDic) == 0:
            print("oneri yok")
        else:
            print("onerilenler : ")
            for i in range(kelimeFrekans):
                boskarakter = ""
                max = 0
                for k in sozluk:
                    if (sozluk[k] > max):
                        max = sozluk[k]
                        boskarakter = k
                    print(boskarakter)

    myDic = histogram(histogramList)
    kelimeFrekans = maxHistogram(myDic)
    maxKelimeler.append(kelimeFrekans)
    writeOutput(maxKelimeler)
    histogramList.clear()


def main():
    readFile(text)
    kontrol(text)
    writeInput()
    readInput()

main()

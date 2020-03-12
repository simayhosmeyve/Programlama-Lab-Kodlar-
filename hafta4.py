import os
os.getcwd()

#Dosyadan texti çeken fonksiyon
def get_words(my_file=u"C:\\Users\\Hp\\Documents\\data.txt"):
    my_list=[]
    f=open(my_file,"r+")
    contents=f.readlines()
    for line in contents:
        #print(line) 
        #Cümle olarak yazdırıyor
        words=line.split(" ")
        for word in words:  
            #Kelime yazdırıyor
            #print(word)
            my_list.append(word) #Listeye kelimeleri ekliyor
            #print(contents) 
    f.close()
    return my_list

#Listenin histogramını tutan fonksiyon
def get_hist(my_list):
    my_hist={}
    for w in my_list:
        if w in my_hist.keys():
            my_hist[w]=my_hist[w]+1
        else:
            my_hist[w]=1
    return my_hist


def get_files(path_1):
    file_s = [file for file in my_list if os.path.isfile(file)]
    return file_s

lst_1=get_words()
get_hist(lst_1)

import os
my_list=os.listdir()

for item in my_list:
    if os.path.isdir(item):
        print(item)
    if os.path.isfile(item):
        print(item)

dir_s =[dir for dir in my_list if os.path.isdir(dir)]   
file_s=[file for file in my_list if os.path.isfile(file)]  
dir_s,file_s
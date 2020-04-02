import random
def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_)) 

    return numbers
get_n_random_numbers()

def frekans(list_1): 
    fre_dict={}
    for item in list_1:
        if (item in fre_dict):
            fre_dict[item]+=1
        else:
            fre_dict[item]=1
    return fre_dict

def frekans_listof_tuples(list_1):
    frekans_list = []
    for i in range(len(list_1)):
        s = False
        for j in range(len(frekans_list)):
            if list_1[i]==frekans_list[j][0]:
                frekans_list[j][1]=frekans_list[j][1]+1
                s=True
        if s == False:
            frekans_list.append([list_1[i],1])
    return frekans_list
 
#Histogram ile listenin modu
def dict_mod(Dic):
    frekans_max= -1 #Hafıza amaçlı değer
    mod=-1
    for key in dic1.keys():
        if dic1[key]>frekans_max:
            frekans_max=dic1[key]
            mod=key
    return mod,frekans_max

def tuples_mod(list_1):
    frekans_max= -1
    mod=-1
    for item,repetition in list2:
        if repetition>frekans_max:
            frekans_max=repetition
            mod=item
    return mod,frekans_max

    
my_list=get_n_random_numbers(15,-4,4)
print(sorted(my_list))
dic1=frekans(my_list)
list2=frekans_listof_tuples(my_list)
print("Mod:",dict_mod(dic1))
print("Mod:",tuples_mod(list2))


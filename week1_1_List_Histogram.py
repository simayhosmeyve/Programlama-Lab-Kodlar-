#n tane elemanı olan bir liste oluşturma

import random
def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_)) 

    return numbers
get_n_random_numbers()

#histogram

#1. yöntem
def frekans(list_1): #değer, frekans gösterir
    fre_dict={}
    for item in list_1:
        if (item in fre_dict):
            fre_dict[item]+=1
        else:
            fre_dict[item]=1
    return fre_dict

#2. yöntem
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
    
my_list=get_n_random_numbers(15,-4,4)
print(sorted(my_list))
print("Dictionary ile:",frekans(my_list))
print("List of tuples ile:",frekans_listof_tuples(my_list))


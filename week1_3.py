import random
def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_)) 

    return numbers
get_n_random_numbers()

#Linear search
def linear_Search(list_1,item_search):
    found =(-1,-1) #default, listede yoksa
    for i in range(len(list_1)):
        if list_1[i] ==item_search:
            found=(i,item_search)
            break
    return found

#Listenin ortalaması
def list_ortalama(list_1):
    n = len(list_1)
    toplam= 0
    for i in range (n):
        toplam = toplam+list_1[i]
    return toplam/n
    
#Liste sıralama(bubble sort)
def bubbleSort(list_1):
    for i in range(len(list_1)-1,-1,-1):
        for j in range(0,i):
            if not (list_1[j]<list_1[j+1]):
                temp = list_1[j]
                list_1[j]=list_1[j+1]
                list_1[j+1]=temp

#Binary search(sıralı liste ile)
def my_Binary_Search(list_1,item_search):
    found=(-1,-1)
    low = 0
    high = len(list_1)-1
    
    while low<=high:
        mid = (low+high)/2
        if list_1[mid]==item_search:
            return list_1[mid],mid
        elif mid>item_search:
            high = mid-1
        else:
            low =mid+1
    return found

#Dizinin medyanı
def median_list(list_1):
    n = len(list_1)
    if n%2==1:
        mid = (n-1)//2
        return list_1[mid]
    else:
        middle_1 = n//2-1
        middle_2=n//2
        ortalama = (list_1[middle_1]+list_1[middle_2])/2
        return ortalama
        
my_list=get_n_random_numbers(15,-4,4)
print(sorted(my_list))
print(linear_Search(my_list,3))
print(list_ortalama(my_list))
print(my_Binary_Search(my_list,3))
print(median_list(my_list))

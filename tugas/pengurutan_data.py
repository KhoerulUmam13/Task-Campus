
print(5*"=",'1. bubble sort',5*"=")
def bubble_sort(list):
    
    a = 0
    for i in range (len(list)-1):
        for j in range (len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
        a+=1
        print(a,list)

datalist = [320,160,420,500,330,120,140,250,110,160,200,230]
print(f"data sebelum diurutkan: {datalist}")
print("hasil dengan bubble sort : ")
bubble_sort(datalist)


print(5*"=",'2. insertion sort',5*"=")
def insertion_sort(a):
    j=0
    for i in range (len(a)-1,-1,-1):
        value = a[i]
        while i < (len(a)-1) and a[i+1] < a[i]:
            a[i] = a[i+1]
            i+=1
            a[i] = value
        print(a)

datalist = [320,160,420,500,330,120,140,250,110,160,200,230]
print(f"data sebelum di urutkan ={datalist}")
print("hasil dengan insertion sort :")
insertion_sort(datalist)

print(5*"=",'3. quick sort',5*"=")
def quick_sort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quick_sort(alist, start, p)
        quick_sort(alist, p + 1, end)

def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] >= pivot):
            i+=1
        while (i <= j and alist[j] <= pivot):
            j-=1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j

datalist = [320,160,420,500,330,120,140,250,110,160,200,230]
print(f"Data sebelum diurutkan : {datalist}")
print("\n")
quick_sort(datalist, 0, len(datalist))
print(f"hasil dengan Quick Sort : {datalist}")


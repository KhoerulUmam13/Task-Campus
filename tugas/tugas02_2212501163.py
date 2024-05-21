
print("\n=====================01=================\n")

for i in range(10,100,10):
    if i <= 100:
     print(i+10,end=" ")

print("\n=====================02=================\n")

i =100
while (i >= 55):
    print(i, end=" ")
    i = i-5


print("\n=====================03=================\n")

i = 1
while (i <= 1024):
    print(i, end=" ")
    i = i*2
    

print("\n=====================04=================\n")
n = int(input("masukan batas perulangan : "))
a = int(input("nilai tabungan awal : "))
b = 0.02


for i in range(0,n):
    c = a*b
    a = a+c

    print(f"bulan ke-{i}",a)



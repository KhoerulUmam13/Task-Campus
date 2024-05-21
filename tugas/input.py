
print("\nSOAL NO.1")
print("\n",5*"=","perintah input",5*"=","\n")

i = 5
n = int(input("masukan jumlah perulangan : "))
while i <= n:
    file = open("/Users/User/Documents/New folder/workspace/latihan python/data_kontak.csv","r+")
    a = file.read()
    print(a)
    b = input("masukan data : ")
    a = (f"{i} {b}\n")
    file.write(a)
    file.close()
    i+=1
    

print("\nsoal no.2")
print("\n",5*"=","perintah cetak dengan data list",5*"=","\n")

with open("/Users/User/Documents/New folder/workspace/latihan python/data_kontak.csv",mode="r") as file:
    print(f"status terbaca = {file.readable()}")
    file.replace("\n","").split(" ")
    print(file.readlines())
    
print("\nsoal no.3")
print("\n",5*"=","perintah cetak dengan data dictionary",5*"=","\n")

with open("/Users/User/Documents/New folder/workspace/latihan python/data_kontak.csv",mode="r") as file:
    print(f"status terbaca = {file.readable()}")
    data = file.readlines()

a = data[0].replace("\n","").split(",")
b = []
for baris in data:
    baris_data = baris.replace("\n","").split(",")
    dict_data = dict()
    for i in range(len(baris_data)):
        dict_data[a[i]] = baris_data[i]
    b.append(dict_data)
print(b)

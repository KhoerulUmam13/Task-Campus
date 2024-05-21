kata = input("Input Kata : ")
temp = ""
for i in range(len(kata)-1, -1, -1): 
    temp+=kata[i]
print("Hasil : ", end="")

if(kata == temp):
    print("Palindrom")
else:
    print("Bukan Palindrom")
    
    


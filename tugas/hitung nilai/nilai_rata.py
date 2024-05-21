import input_nilai

def nilai_rata():
    n = input("masukan banyak data : ")
    data = []
    jum = 0
    for i in range(0,n):
        temp = int(input("masukan nilai ke-%d : "%(i+1)))
        data.append(temp)
        jum += data [i]
        rata2 = jum / n
    print("rata rata = %0.2f"% rata2)    
    return nilai_rata
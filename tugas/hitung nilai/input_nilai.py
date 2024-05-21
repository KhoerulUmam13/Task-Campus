def fungsi_nilai_total(var_harian,var_uts,var_uas):
    var_harian = int(var_harian) * 0.3
    var_uts = int(var_uts) * 0.3
    var_uas = int(var_uas) * 0.4
    
    var_total = var_harian + var_uts + var_uas
    return var_total
def fungsi_percabangan (var_nilai):
    var_huruf = ""
    if (var_nilai >= 0 and var_nilai < 20):
        var_huruf = "E"
    elif(var_nilai >= 20 and var_nilai < 40):
        var_huruf = "D"
    elif(var_nilai >= 40 and var_nilai < 60):
        var_huruf = "C"
    elif(var_nilai >= 60 and var_nilai < 80):
        var_huruf = "B"
    elif(var_nilai >= 80 and var_nilai < 100):
        var_huruf = "A"
    return var_huruf
def fungsi_perulangan():
    var_hasil_perulangan = 0
    for i in range(1,3):
        print("nilai ke",i,"---")
        var_harian = input("nilai tugas : ")
        var_uts = input("nilai uts : ")
        var_uas = input("nilai uas : ")
        var_hasil_perulangan += (int(fungsi_nilai_total(var_harian,var_uts,var_uas)))
    return var_hasil_perulangan


var_total = fungsi_perulangan()

print("----------total nilai-----------")
print("total nilai yang di dapat : ",var_total)
print("total nilai dalam hurup : ",fungsi_percabangan(var_total))


n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())

    result1 = (a + b) // c
    result2 = (a * b) % c

    print(result1, result2)

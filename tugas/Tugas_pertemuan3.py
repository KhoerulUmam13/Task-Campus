
# NAMA = KHOERUL UMAM
# NIM = 2212501163
# KELAS = XA A1
print("\n============no.1=============\n")

import math

a = 1
b = -2
c = 1

d = (b**2) - (4*a*c)

x1 =(-b + math.sqrt(d))/(2**a)
x2 =(-b - math.sqrt(d))/(2**a)

y1 = a * (x1**2) + (b*x1) + c
y2 = a * (x2**2) + (b*x2) + c

print(y1)
print(y2)
print(x1)
print(x2)

print("\n=================no.2===================\n")
m = float(input("masa benda (kg)       : "))
v = float(input("kecepatan benda (m/s) : "))

v_kuadrat = v ** 2
ek = (1/2) * m * v_kuadrat
print("=========================================\n")
print("masa : ",m,"kg")
print("kecepatan : ",v,"m/s")
print("masa : ",ek,"J")



print("\n=================no.3=====================\n")

tarif_listik = int(input("masukan tarif : Rp. "))
kwh_awal = int(input("jumlah KWH awal : "))
kwh_akhir = int(input("jumlah KWH akhir : "))

print("==========================================")

jumlah_kwh = (kwh_akhir - kwh_awal)
total_tagihan = (jumlah_kwh * tarif_listik)
print("jumlah KWH yang terpakai : ", jumlah_kwh)
print("total tagihan listrik : ", total_tagihan)



print("\n=====================no.4=====================\n")
gaji_pokok = int(input("gaji pokok : Rp. "))
uang_transport = int(input("uang transpot : Rp. "))
jumlah_kehadiran = int(input("hadir : " ))
bayar_pajak = int(input("pajak : Rp. "))
print("\n==========================================\n")
total_transport = uang_transport * jumlah_kehadiran
total_gaji = gaji_pokok + total_transport
pajak = (10/100) * total_gaji
gajih_bersih = gaji_pokok - bayar_pajak

print("total gajih : Rp. ", total_gaji)
print("pajak : ", pajak)
print("gajih bersih : Rp. " ,gajih_bersih)



print("\n===================no.5====================\n")

masuk  = int(input("jam masuk : "))
menit_masuk = int(input("menit masuk : "))
keluar = int(input("jam keluar : "))
menit_keluar = int(input("menit keluar : "))
biaya_parkirperjam = 1000

print("\n========================================\n")

total_menit = (keluar * 60 + menit_keluar) - (masuk * 60 + menit_masuk)
lama_parkir = total_menit / 60
harga = lama_parkir * biaya_parkirperjam

print("total menit : ",total_menit)
print("lama parkir : ",lama_parkir)
print("total tagihan parkir : ",harga)
print("\n")



print("\n=======================no.6==========================\n")
jumlah_pinjaman = int(input("jumlah yang di pinjam : "))
lama_pinjaman   = int(input("bulan : "))
bunga_pinjaman  = float(input("bunga : "))
biaya_ADM       = int(input("admin : "))

print("\n==========================================\n")

jumlah_angsuran = jumlah_pinjaman * bunga_pinjaman
jumlah_bunga    = (8/100)*jumlah_pinjaman
total_angsuran  = jumlah_angsuran + jumlah_bunga


print("jumlah pinjaman : ",jumlah_pinjaman)
print("lama pinjaman : ",lama_pinjaman)
print("total angsuran : ",total_angsuran)
print("\n")
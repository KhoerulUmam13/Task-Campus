
from Kelas_gajiBersih import hitung_gajibersih
from tabulate import tabulate

list_karyawan = []

def hitung_totalhonor(honor, jumlah_hadir):
    return honor*jumlah_hadir

def hitung_gajikotor(total_honor, tunjangan):
    return total_honor+tunjangan

def hitung_pajak(total_gajikotor):
    return total_gajikotor*0.0225

n = int(input("Masukkan jumlah karyawan yang diinput : "))
i=0
while i < n:
    try:
        kdkaryawan = input("kode karyawan: ")
        nama_karyawan = input("nama karyawan: ")
        tunjangan = int(input("tunjangan: "))
        honor = int(input("honor: "))
        jml_Hadir = int(input("jumlah hadir: "))

        total_Honor = hitung_totalhonor(honor, jml_Hadir)
        total_Gaji_Kotor = hitung_gajikotor(total_Honor, tunjangan)
        pajak = hitung_pajak(total_Gaji_Kotor)
        gajiBersih = hitung_gajibersih(total_Gaji_Kotor, pajak)

        list_karyawan.append([
            kdkaryawan,
            nama_karyawan,
            '{:,}'.format(tunjangan),
            '{:,}'.format(honor),
            jml_Hadir,
            '{:,.2f}'.format(total_Honor),
            '{:,.2f}'.format(total_Gaji_Kotor),
            '{:,.2f}'.format(pajak),
            '{:,.2f}'.format(gajiBersih)
        ])
        i+=1
        
        print(f"\n{i}. Karyawan {nama_karyawan} berhasil ditambahkan!","\n")
        print(tabulate(list_karyawan, headers= ['kdkaryawan', 'nama_karyawan', 'tunjangan', 'honor', 'jmlHadir', 'total_Honor', 'total_gaji_kotor', 'pajak', 'honor_bersih'], tablefmt="orgtbl"))

        for data in list_karyawan:
            kdkaryawan = data[0],
            nama_karyawan = data[1],
            tunjangan = data[2],
            honor = data[3],
            jmlHadir = data[4],
            total_Honor = data[5],
            total_gaji_kotor = data[6],
            pajak = data[7],
            honor_bersih = data[8]
    except ValueError:
        print('data yang ada masukan salah,silahkan coba lagi!!!')
    
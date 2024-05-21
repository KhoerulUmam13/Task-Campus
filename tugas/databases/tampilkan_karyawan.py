import mysql.connector
from    mysql.connector import errorcode
from tabulate import tabulate
db_2212501163_a = {
   'user' : 'root',
    'password' : '',
    'host' : 'localhost',
    'database' : 'db_2212501163_a'
    }
koneksi = mysql.connector.connect(**db_2212501163_a)

if koneksi.is_connected():
    print("Berhasil terhubung")
else:
    print("Gagal terhubung")
koneksi = mysql.connector.connect(**db_2212501163_a)
kursor = koneksi.cursor()

#tampil
print('NAMA : KHOERUL UMAM')
print('NIM  : 2212501163')
print(5*'=','menampikan data',5*'=')

sql = "SELECT * FROM instruktur"
kursor.execute(sql)
print(tabulate(kursor, headers= ['kdkaryawan', 'nama_karyawan', 'tunjangan', 'honor', 'jmlHadir', 'total_Honor', 'total_gaji_kotor', 'pajak', 'honor_bersih'], tablefmt="orgtbl"))

for row in kursor:
    kdkaryawan = row[0],
    nama_karyawan = row[1],
    tunjangan = row[2],
    honor = row[3],
    jmlHadir = row[4],
    total_Honor = row[5],
    total_gaji_kotor = row[6],
    pajak = row[7],
    honor_bersih = row[8]

    print(kdkaryawan, nama_karyawan, tunjangan, honor, jmlHadir,total_Honor, total_gaji_kotor, pajak, honor_bersih)
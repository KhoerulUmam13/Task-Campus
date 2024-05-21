import mysql.connector
from mysql.connector import errorcode

db_2212501163_a = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_2212501163_a'
}
koneksi = mysql.connector.connect(**db_2212501163_a)
if koneksi.is_connected():
    print("terhubung")
else:
    print("tidak terhubung")

print('NAMA : KHOERUL UMAM')
print('NIM  : 2212501163')
print(5*'=', 'menambahkan data', 5*'=')

dict_instruktur = {}
kdkarywan = input("Masukkan kode karyawan : ")
nama_karyawan = input("Masukkan Nama karyawan : ")
tunjangan = input("Masukkan tunjangan : ")
honor = input("Masukkan honor : ")
jmlHadir = int(input("Masukkan kehadiran : "))
total_Honor = int(input("Masukkan total honor : "))
total_GajiKotor = int(input("Masukkan gaji kotor : "))
pajak = float(input("Masukkan pajak : "))
honorBersih = float(input("Masukkan honor bersih : "))

dict_instruktur['kdkaryawan'] = kdkarywan
dict_instruktur['nama_karyawan'] = nama_karyawan
dict_instruktur['tunjangan'] = tunjangan
dict_instruktur['honor'] = honor
dict_instruktur['jmlHadir'] = jmlHadir
dict_instruktur['total_Honor'] = total_Honor
dict_instruktur['total_gaji_kotor'] = total_GajiKotor
dict_instruktur['pajak'] = pajak
dict_instruktur['honor_bersih'] = honorBersih

nama_db = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_2212501163_a'}
koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()
sql = ("INSERT INTO instruktur(kdkaryawan, nama_karyawan, tunjangan, honor, jmlHadir, total_Honor, total_gaji_kotor, pajak, honor_bersih) VALUES (%(kdkaryawan)s, %(nama_karyawan)s, %(tunjangan)s, %(honor)s, %(jmlHadir)s, %(total_Honor)s, %(total_gaji_kotor)s ,%(pajak)s, %(honor_bersih)s)")
kursor.execute(sql, dict_instruktur)
koneksi.commit()
print("{} data telah ditambahkan".format(kursor.rowcount))
koneksi.close()

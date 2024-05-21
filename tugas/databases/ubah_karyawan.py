import mysql.connector
from    mysql.connector import errorcode
db_2212501163_a = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'db_2212501163_a'
}
koneksi = mysql.connector.connect(**db_2212501163_a)
if koneksi.is_connected():
    print("terhubung")
else:
    print("tidak terhubung")

print('NAMA : KHOERUL UMAM')
print('NIM  : 2212501163')
print(5*'=','mengubah data',5*'=')

import mysql.connector
dict_instruktur = {}
kdkarywan = input("Masukkan kode karyawan : ")
nama_karyawan = input("Masukkan Nama karyawan : ")
tunjangan = input("Masukkan tunjangan : ")
honor = input("Masukkan honor : ")
jmlHadir = int(input("Masukkan kehadiran : "))
total_Honor = int(input("Masukkan total honor : "))
total_GajiKotor = int(input("Masukkan gaji kotor : "))
pajak = int(input("Masukkan pajak : "))
honorBersih = int(input("Masukkan honor bersih : "))

dict_instruktur ['kdkaryawan'] = kdkarywan
dict_instruktur ['nama_karyawan'] = nama_karyawan
dict_instruktur ['tunjangan'] = tunjangan
dict_instruktur ['honor'] = honor
dict_instruktur ['jmlHadir'] = jmlHadir
dict_instruktur ['total_Honor'] = total_Honor
dict_instruktur ['total_gaji_kotor'] = total_GajiKotor
dict_instruktur ['pajak'] = pajak
dict_instruktur ['honor_bersih'] = honorBersih

nama_db= {
  'user' : 'root', 
  'password' : '', 
  'host' : 'localhost',
  'database' : 'db_2212501163_a' }
koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

sql = ("UPDATE instruktur SET nama_karyawan = %(nama_karyawan)s , tunjangan = %(tunjangan)s , honor = %(honor)s , jmlHadir = %(jmlHadir)s , total_Honor = %(total_Honor)s , total_gaji_kotor = %(total_gaji_kotor)s , pajak = %(pajak)s , honor_bersih = %(honor_bersih)s WHERE kdkaryawan = %(kdkaryawan)s")


kursor.execute(sql, dict_instruktur)
koneksi.commit()
print("{} data telah diubah".format(kursor.rowcount))
koneksi.close()


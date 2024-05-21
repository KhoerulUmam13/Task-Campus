import mysql.connector
from    mysql.connector import errorcode

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


#mengapus
print('NAMA : KHOERUL UMAM')
print('NIM  : 2212501163')
print(5*'=','menghapus data',5*'=')

dict_instruktur = {} 
kdkaryawan = input("Masukkan kode karyawan : ")

dict_instruktur ['kdkaryawan'] = kdkaryawan

nama_db = {
  'user' : 'root',
  'password' : '',
  'host' : 'localhost',
  'database' : 'db_2212501163_a'}

koneksi = mysql.connector.connect(**db_2212501163_a)
kursor = koneksi.cursor()
sql = ("DELETE FROM instruktur WHERE kdkaryawan = %(kdkaryawan)s ")
kursor.execute(sql, dict_instruktur)
koneksi.commit()
print("{} data telah dihapus".format(kursor.rowcount))
koneksi.close()
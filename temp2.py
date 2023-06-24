from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='library_team')
cursor = cnx.cursor()

query = ("SELECT * "
         "FROM author "
         )

cursor.execute(query)

# for (id_nasabahFK, jenis_transaksi, tanggal, jumlah) in cursor:
#     print("nasabah dengan ID {} melakukan transaksi {} pada {:%d %b %Y} sejumlah {}".format(
#         id_nasabahFK, jenis_transaksi, tanggal, jumlah
#     ))

print(cursor.fetchall())
cursor.close()
cnx.close()

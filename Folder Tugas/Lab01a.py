# input nama dari pengguna
nama = input("Masukkan nama anda: ")

#input tahun kelahiran pengguna
tahun = int(input("Masukkan tahun kelahiran anda: "))
umur = 2020 - tahun
umur_str = str(umur)

#input tempat tinggal pengguna
tempat = input("Masukkan tempat tinggal anda: ")

#Assign Biodata
biodata = nama + " berumur " + umur_str + " tahun, tinggal di " + tempat

#Cetak biodata pengguna
print(biodata)
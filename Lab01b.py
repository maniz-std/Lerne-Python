#asumsikan 1 bulan = 30 hari, 1 tahun = 365 hari

#Input Jumlah Hari
hari = int(input("Masukkan jumlah hari: "))

#Sisa Hari
sisa_hari = hari%365

#konversi hari menjadi tahun
tahun = int(hari / 365)

#konversi hari menjadi bulan
bulan = int(sisa_hari / 30)
sisa_hari2 = sisa_hari%30

#konversi hari menjadi minggu
minggu = int(sisa_hari2/7)
sisa_hari3 = sisa_hari2%7

#output
print(hari, "hari adalah", tahun, "tahun", bulan, "bulan", minggu, "minggu, dan", sisa_hari3, "hari")
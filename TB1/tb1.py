#Fajri Ramadhan
#41822010049
import re

with open('input.txt', 'r') as file:
    baris_file = file.readlines()

baris_pertama = baris_file[0].strip().split()
jumlah_baris = int(baris_pertama[0])
jumlah_kolom = int(baris_pertama[1])

matriks = [baris_file[i + 1].strip() for i in range(jumlah_baris)]

hasil_akhir = ""
for kolom in range(jumlah_kolom):
    for baris in range(jumlah_baris):
        if kolom < len(matriks[baris]):
            hasil_akhir += matriks[baris][kolom]

pola = r'(?<=[\w])[^\w]+(?=[\w])'
hasil_akhir = re.sub(pola, ' ', hasil_akhir)

print(hasil_akhir)

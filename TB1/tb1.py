#Fajri Ramadhan
#41822010049
import re
with open('input.txt', 'r') as file:

    input_masukan = file.readline().rstrip().split()
    n = int(input_masukan[0])
    m = int(input_masukan[1])

    matriks = []
    for _ in range(n):
        item_matriks = file.readline().rstrip()
        matriks.append(item_matriks)

hasil_dekode = ""

for i in range(m):
    for j in range(n):
        try:
            hasil_dekode += matriks[j][i]
        except IndexError:
            pass

pola = r'(?<=[\w])[^\w]+(?=[\w])'
pola_hasil = re.findall(pola, hasil_dekode)

for x in pola_hasil:
    hasil_dekode = hasil_dekode.replace(x, ' ', 1)

print(hasil_dekode)

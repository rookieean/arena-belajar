# soal pertama
print("-------soal pertama------")
harga_tiket = 50000

usia = int(input("usia pengunjung = "))

if usia < 12:
    harga_diskon = harga_tiket * 0.5
elif usia >= 60:
    harga_diskon = harga_tiket * 0.3
else:
    harga_diskon = harga_tiket

print(f"Harga tiket yang harus dibayar: Rp {harga_diskon:.3f}")


# soal kedua
print("-----------soal kedua-----------")

tahun = int(input("Masukkan tahun: "))

if (tahun % 4 == 0):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")



#soal ketiga
print("---------soal ketiga-------------")

nilai = float(input("masukan nilai akhir ="))

if nilai > 80:
    grade = 'LULUS'
elif nilai < 80:
    grade = 'COBA LAGI'

print(f'Grade: {grade}')

# soal keempat
print("------soal ketiga---------")

x = float(input("masukan nilai x :"))
y = float(input("masukan nilai y :"))

P = x + y

if P >= 0:
    Q = x * y
elif P <= 0:
    Q = x / y

print(f'nilai Q = {Q}')

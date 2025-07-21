

"""
Tulislah sebuah program yang mengambil serangkaian angka yang dipisahkan oleh koma dan spasi, dan mengeluarkan jumlah angka-angka tersebut. Program harus menangani angka negatif dan mengasumsikan formatnya konsisten.
"""


# yang gua bikinnnn....
num = {}
amnt = 0

for number in num:
    amnt += num

print(amnt)



# yang berhasil
s = input()
a = s.split(', ') # yang memisahkan koma dan spasi
total = 0
for d in a:
    total += int(d)
print(total)
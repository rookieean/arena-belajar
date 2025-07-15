"""
    pertemuan 2 soal
    
        1. buatlah algoritma/flowchart untuk menginputkan 3 buah bilangan bulat dan tampilkan bilangan terbesar diantara ketiganya(dianggap  ketiga bilangan nilainya berbeda) tidak boleh menggunakan operator logika

"""

def DINOSAURUS(a, b, c):
    return max(a, b, c)


a = 4
b = 7
c = 8

a = int(input("masukkan bilangan pertama: "))
b = int(input("masukkan bilangan kedua: "))
c = int(input("masukkan bilangan ketiga: "))

print("hasilnya adalah", DINOSAURUS(a, b, c))





"""""
if a == b:
    print ("Sama SISI")
else:
    print ("sama kaki")

print("sembarang")
"""""
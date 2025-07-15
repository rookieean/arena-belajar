"""
Penanganan berkas merupakan bagian penting dari setiap aplikasi web.

Python memiliki beberapa fungsi untuk membuat, membaca, memperbarui, dan menghapus file.
"""
# open() -> membuka file

# ada 4 metode/mode untuk membuka file:
# "r" -> baca -- Membuka file untuk dibaca, kesalahan jika file tidak ada
# "a" -> tambahkan -- Membuka file untuk ditambahkan, membuat file jika belum ada
# "w" -> tulis -- Membuka file untuk ditulis, membuat file jika belum ada
# "x" -> buat -- Membuat file yang ditentukan, mengembalikan kesalahan jika file tersebut ada

# kamu bisa menangani file dibuat format apa:
#"t" -> format teks
# "b" -> biner

# contoh
f = open("tryme.txt", "rt")
# buka file tryme.txt trus baca tampilkan format teks



"""
----------------------------- Buka File Python ------------------------
"""

# BUKA FILE DI SERVER
"""
contoh ada file seperti ini


file demo.txt

Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
"""

f = open("demofile.txt", "r")
print(f.read())

# jika berkas ada di lokasi lain
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

# mau baca filenya beberapa bagian aja
f = open("demofile.txt", "r")
print(f.read(5)) # baca 5 karakter pertama dri file

# baca se baris
f = open("demofile.txt", "r")
print(f.readline()) # baca satu baris
print(f.readline()) # baca dua baris

# ato bisa gini gengs
f = open("demofile.txt", "r")
for x in f:
    print(x)


# Tutup File
f = open("demofile.txt", "r")
print(f.readline())
f.close()
#  Anda harus selalu menutup berkas Anda. Dalam beberapa kasus, karena buffering, perubahan yang dibuat pada berkas mungkin tidak terlihat hingga Anda menutup berkas tersebut.



"""
------------------------ Penulisan File Py ----------------
"""

# MENULIS KE FILE YANG ADA

# "a" -> tambahkan -- menambahkan keakhir file
# "w" -> tulis -- menimpa konten apa pun yang ada

# buka file demotext.txt dan tambahkan konten ke file
f = open("demofile.txt", "a")
f.write("now the file has more content!")
f.close()

# membuka dan membaca file setelah ada penambahan
f = open("demofile.txt", "r")
print(f.read())


# buka file dan timpa kontennya
f = open("demofiletxt.txt", "w")
f.write("whooops! i have deleted")
f.close()

f = open("demofile.txt", "r")
print(f.read())

# buat file baru
# "x" -> buat
# "a" -> tambahkan
# "w" -> tulis

f = open("myfile.txt", "x")
# file kosong baru tercipta
f = open("myfile.txt", "w")



"""
---------------------------- Hapus File Python ----------------
"""

# Hapus file
# harus pake modul OS
import os
os.remove("demofile.txt")

# cek dulu, filenya ada gak, sebelum dihapus
import os
if os.path.exists("demofile.txt"):
   os.remove("demofile.txt")
else:
    print("the file does not exist!")

# hapus folder kosong
import os
os.rmdir("myfolder")

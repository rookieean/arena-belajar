"""
            w3schools - 
"""

print("""
[]_____Game OF Thrones______[-][o][x]
|                                   |
|       Welcome to Mini Games       |
| Please fill the correct item here |
|                                   |
|                                   |
|===================================|
""")

thislist = ["apple", "banana", "cherry", "mango", "kiwi", "tomato"]
print(thislist[-0])
print(thislist[-1])
print(thislist[-2])
print(thislist[0])
print(thislist[1])
print(thislist[2])

if "nanas" in thislist:
    print("Yes, are u there")
else:
    print("\noh no,..")

# changed item value
thislist[2] = "blackberry"
print("result of answer", thislist)

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])
print(mylist)

# with append
aironman  = ["black widow", "maroon", "curves"]
aironman.append("tuk"  + "lang" + "ndes")
print(aironman)
# with insert
aironman.insert(3, "changcutters")
print(aironman)
# with extend - gabung dua kelompok jadi satu
anvengers = ["optimus", "jaquard", "avangeline", "panthom"]
stabilo = ("lokk", "baron", "wish" )
anvengers.extend(stabilo)
print(anvengers)


mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist)

"""
                Remove List Items

"""

# remove method
AlatDapur = ["centong", "wajan", "cobek", "irus"]
AlatDapur.remove("irus")
print(AlatDapur)

# pop method
AlatDapur.pop(2) # AlatDapur.pop() -> kosong yg di eksekuis yg last item
print(AlatDapur)

# del method
del AlatDapur[0]
print(AlatDapur)

# clear methods
AlatDapur.clear()
print(AlatDapur)

"""
                Loop Lists
"""

# for loop
MenuPadang = ["ayam goreng", "telur balado", "ati ampela", "udang krispy"]
for x in MenuPadang:
    print(x)

# range + len
MenuPadang = ["ayam goreng", "telur balado", "ati ampela", "udang krispy"]
for ngeleh in range(len(MenuPadang)):
    print(MenuPadang[ngeleh])

# while + len
MenuPadang = ["jagung manis", "ayam goreng", "telur balado", "ati ampela", "udang krispy"]
he = 0
while he < len(MenuPadang):
    print(MenuPadang[he])
    he = he + 1

# for pendek
MenuPadang = ["jagung manis", "ayam goreng", "telur balado", "ati ampela", "udang krispy"]
[print(x) for x in MenuPadang]

"""
            List Comprehension - Pemahaman Daftar
"""

# example
MenuJajanSekolah = ["cilok", "cilor", "pentol", "tahu goreng"]
JajanBaru = []

for x in MenuJajanSekolah:
    if "a" in x:    # dia nyari yg ada huruf a nya
        JajanBaru.append(x)     # klo dah, ditambah nk JajanBaru

print(JajanBaru)

# atau bisa gini juga,..
JajanPart2 = [x for x in MenuJajanSekolah if "a" in x]
print(JajanPart2)


# sintaksis
"""
    newlist = [expresion for item in iterable if condition == True]
jadi nilai yang dikembalikan adlh daftar baru, tanpa mengurangi daftar lama


---newlist = [x if x != "banana" else "orange" for x in fruits]
 "KEMBALIKAN BARANGNYA KALAU BUKAN PISANG, KALAU PISANG KEMBALIKAN JERUK"
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print( "newlist ", newlist)
# KASIH PISANG, ATAU JERUK NK GK ADA

"""
            Sort Lists - List Pendek
"""

# sort -> mengurutkan dri yag paling kecil
numberYup = [100, 29, 67, 10, 20, 47, 28, 10]
numberYup.sort()
print(numberYup)

# reverse = True -> mengurutkan dri yg paling besar
numberYup.sort(reverse=True)
print(numberYup)

# Fungsi ini akan mengembalikan angka yang akan digunakan untuk mengurutkan daftar (angka terendah terlebih dahulu)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# diurutkan dri abjad huruf besar A-a
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# str.lower dri a - A
this = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# balik susunan apapun abjadnya -> acak item
thislist.reverse()
print(thislist)

"""
        Copy Lists - Salin Daftar
"""

# salin daftar a ke daftar b

# copy() -> salin daftar
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# list()
mylist = list(thislist)
print(mylist)

# irisan operator [:]
mylist = thislist[:]
print(mylist)

"""
        Join Lists - Gabungkan Daftar
"""

# cara gabungin dua list
GeprekSauce = ["trasi", "geprek", "bawang jog", "sus"]
Minum = ["es jumbo", "krampul", "jeruk dingin"]

Gabung = GeprekSauce + Minum
print(Gabung)

# extend()
Gabung.extend(Minum)
print(Gabung)

# append()
for x in Minum:
    GeprekSauce.append(x)

print(GeprekSauce)

"""
        List Methods - Metode Daftar
"""

# append() -> menambahkan item di akhir list
# clear() -> menghapus semua item di list
# copy()  -> mengembalikan salinan list
# count() -> mengembalikan jumlah item dengan nilai tertentu
# extend() -> menambahkan item dari list lain ke list
# index() -> mengembalikan indeks item pertama dengan nilai tertentu
# insert() -> menambahkan item pada posisi tertentu
# pop() -> menghapus item pada posisi tertentu
# remove() -> menghapus item dengan nilai tertentu
# reverse() -> membalik urutan list
# sort() -> mengurutkan list

print("______________________Tuples Python________________________")

"""
               Tuple
    isi itemnya tidak bisa diubah, bisa sama, 
"""

AnekaMolen = ("pisang", "coklat", "keju", "ketan hitam", "strawberry", "ubi")

"""
Koleksi Python (Array)
Ada empat tipe data koleksi dalam bahasa pemrograman Python:

List(daftar) adalah koleksi yang diurutkan dan dapat diubah. Mengizinkan anggota duplikat.
Aneka = ["pisang", "coklat", "keju", "ketan hitam"]


Tuple adalah koleksi yang teratur dan tidak dapat diubah. Mengizinkan anggota duplikat.
AnekaMolen = ("pisang", "coklat", "keju", "ketan hitam")

Set adalah koleksi yang tidak berurutan, tidak dapat diubah*, dan tidak terindeks. Tidak ada anggota yang duplikat.
Aneka = {"pisang", "coklat", "keju", "ketan hitam"}

Dictionary(kamus) adalah koleksi yang teratur** dan dapat diubah. Tidak ada anggota yang duplikat.
Aneka = {"nama": "John", "umur": 36}

"""

AnekaMolen = ("pisang", "coklat", "keju", "ketan hitam", "strawberry", "ubi")

if "ubi" in AnekaMolen:
    print("ada")

# tuple -> gak iso diubah, ditambah, dihapus, 
# ada solusinya lhoo
AnekaMolen = ("pisang", "coklat", "keju", "ketan hitam", "strawberry", "ubi")
DaftarBaru = list(AnekaMolen)
DaftarBaru[1] = "blackcurrant"
AnekaMolen = tuple(DaftarBaru)
print(AnekaMolen)
print(DaftarBaru)

"""
    ubah tuple daftar -> ubah item -> ubah jadi tuple
"""
# gk punya append, remove, pop, clear, insert, extend, sort, reverse
yup = list(AnekaMolen)
DaftarBaru.append("orange")
AnekaMolen = tuple(DaftarBaru)
print(AnekaMolen)
# atau...
DaftarBaru = ("bababa",)
AnekaMolen += DaftarBaru
print(AnekaMolen)

thistuple = ("apple", "banana", "cherry")
y = ("orange")
thistuple += y
print(thistuple)

# remove
DaftarBaru = list(AnekaMolen)
DaftarBaru.remove("orange")
AnekaMolen = tuple(DaftarBaru)
print(AnekaMolen)

# del -> hapus tuple sepeneuhnya
del AnekaMolen

"""
        Bongkar tuple - Unpack Tuple
"""
Aneka = ("pisang", "coklat", "keju", "ketan hitam", "strawberry", "ubi")
(kuning, coklat, *keju, ) = Aneka 
print(kuning)
print(coklat)
print(keju)

# gunanya asterik (*) kanggo sisane item yg kelebihan

"""
        Loop Tuples - Perulangan Tuple
"""
number = (1, 2, 3, 4, 5, 6, 7,  8, 9, 10)

# through
for x in number:
    print(x)

# range + len
for i in range(len(number)):
    print(number[i])

# while + len
i = 2
while i < len(number):
    print(number[i])
    i = i + 1

"""
        Join Two Tuples - Gabungkan Dua Tuple
"""

# by two tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# multiply tuple
tuple4 = tuple1 * 2
print(tuple4)

"""
        Tuple Methods - Metode Tuple
"""
# count() -> mengembalikan jumlah item dengan nilai tertentu
# index() -> mengembalikan indeks item pertama dengan nilai tertentu

"""
        Py set - Set Python
"""

# set -> gak bisa diubah, bisa dihapus, bisa ditambah
# gak bisa diindeks, gak bisa diurutkan
# gak bisa duplikat

Lumer = {"coklat", "tiramisu", "strawberry", "coklat", True, 1, 2}
print("lumer = ", Lumer)
# nilai duplikat diabaikan
# True = 1, juga diabaikan

set1 = {"abc", 34, True, 40, "male"} # bisa campur

"""
        Acess Items - Akses Item
"""

# wrong example
thisset = {"apple", "banana", "cherry"}
while x != "banana":
    print("aku suka", x)
    break

"""
        Add Items - Tambahkan Item
"""
# add() -> menambahkan item
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print({f"thisset = {thisset}"})

# update()
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
print({f"thisset = {tropical}"})

"""
        Remove Item - Hapus Item
"""

# remove() -> hapus item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# discard() -> hapus item
thisset.discard("banana")
print(thisset)

# pop() -> hapus item -> gak tau item apa yg dihapus
x = thisset.pop()
print(x)
print(thisset)

# clear() -> hapus semua item
thisset.clear()
print(thisset)

"""
        Loop Sets - Perulangan Set
"""

# for in
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

"""
        Join Sets - Gabungkan Set   
"""

# union() -> gabungkan dua set
# update() -> gabungkan dua set
# intersection_update() -> hanya item yg sama
# difference_update() -> hanya item yg beda
#symmetric_difference_update() -> item yg beda, gk pake item kembar

# union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
mmyset = set1 | set2 | set3 | set4
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# update()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# intersection_update() / intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection_update(set2)
print(set3)

#
set3 = set1 & set2
print(set3)

#
set1.intersection(set2)
print(set1)

# difference_update() / difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference_update(set2)
print(set3)

#
set3 = set1 - set2
print(set3)

#
set1.difference_update(set2)
print(set1)

# symmetric_difference_update() / symmetric_difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference_update(set2)
print(set3)

#
set3 = set1 ^ set2
print(set3)

#
set1.symmetric_difference_update(set2)
print(set1)

"""
        set methods - Metode Set
"""

# add() -> menambahkan item
# clear() -> menghapus semua item
# copy() -> mengembalikan salinan set
# difference() -> mengembalikan set yang berisi perbedaan antara dua atau lebih set
# difference_update() -> menghapus item dalam set yang juga ada dalam set lain
# discard() -> hapus item
# intersection() -> mengembalikan set yang berisi item yang sama dalam dua set
# intersection_update() -> menghapus item dalam set yang tidak ada dalam set lain
# isdisjoint() -> mengembalikan False jika dua set memiliki setidaknya satu item yang sama, jika tidak mengembalikan True
# issubset() -> mengembalikan True jika semua item dalam set lain ada dalam set, jika tidak mengembalikan False
# issuperset() -> mengembalikan True jika semua item dalam set ada dalam set lain, jika tidak mengembalikan False
# pop() -> menghapus item
# remove() -> menghapus item
# symmetric_difference() -> mengembalikan set yang berisi semua item dari kedua set, kecuali item yang sama
# symmetric_difference_update() -> menyisipkan item yang tidak ada dalam set lain
# union() -> mengembalikan set yang berisi semua item dari set, dan item lainnya dalam set lain
# update() -> menyisipkan item dari set lain ke set

"""
        Dictionary Python
"""
# dapat diubah, urut, tidak boleh ada duplikat

# contoh ketika  ada nilai  duplikat
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2021
}
print(thisdict)

# isi kamus bisa  dengan tipe  data apapun
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(len(thisdict)) # panjang kamus

# konstruktor dict()
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)

"""
        Akses Item - Akses Item
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")
x = thisdict.keys()
# metode tiga baris atas sama saja
print(x)

"""
         ubah Item - Ubah Item
"""

# ubah kunci kamus
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2023 # ubah kunci "year" menjadi 2023
print(thisdict)

# perbarui kamus
thisdict.update({"year": 2023})

"""
        Tambahkan Item - Tambahkan Item
"""

# tambahkan item
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

"""
       ----------------------------- hapus item
"""

# pop() -> hapus item
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# popitem() -> hapus item terakhir
thisdict.popitem()
print(thisdict)

# del -> hapus item dgn nama  kunci
del thisdict["brand"]
print(thisdict)

# clear() -> hapus semua item
thisdict.clear()
print(thisdict)

"""
---------------------- Loop Dictionary - Perulangan Kamus
"""

# for in
for c in thisdict:
    print(c) # output kunci

for c in thisdict:
    print(thisdict[c]) # output nilai dari kunci

# values()
for x in thisdict.values():
    print(x) # output nilai dari kunci

# keys ()
for x in thisdict.keys():
    print(x) # output kunci

# items()
for x, y in thisdict.items():
    print(x, y) # output nilai dan kunci

"""
---------------- Copy Dictionary - Salin Kamus
"""

# copy() -> salin kamus
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# dict() -> salin kamus
mydict = dict(thisdict)
print(mydict)

"""
----------------------------- Nested Dictionaries - Kamus Bertingkat
"""
# kamus bersarang adalah kamus dalam kamus
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
# mengakses item dalam kamus bersarang
print(myfamily["child1"]["name"])

# ulangi melalui kunci dan nilai  dari semua kamus bersarang
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ":", obj[y])

"""
output dari variabel myfamily jika hanya pakai
print(myfamily) akan kasih output isi dari kamus myfamily

sedang kalau pakai perulangan for i....., bakal kasih output sama, cuma lebih rapi
"""

# clear() -> hapus semua item
# copy() -> salin kamus
# fromkeys() -> kembalikan kamus dengan kunci dan nilai yang ditentukan
# get() -> kembalikan nilai dari kunci yang ditentukan
# items() -> kembalikan daftar yang berisi tuple pasangan kunci / nilai
# keys() -> kembalikan daftar yang berisi kunci
# pop() -> hapus item dengan kunci yang ditentukan
# popitem() -> hapus item terakhir
# setdefault() -> kembalikan nilai dari kunci yang ditentukan. Jika kunci tidak ada: masukkan kunci dengan nilai yang ditentukan
# update() -> memperbarui nilai kunci yang ada
# values() -> kembalikan daftar nilai

"""
        Python If ... Else
"""

# if 
a = 33
b = 200
if b > a:
    print("b is greater than a")

# elif = jika kondisi pertama salah, coba yang ini
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# else = jika kondisi pertama dan kedua salah, coba yang ini
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# operator terner -> di tulis hanya dalam satu baris saja
a = 2
b = 330
print("A") if a > b else print("B") # yg dimaksud satu baris

# bisa pakai if else
print("A") if a > b else print("=") if a == b else print("B")

# bisa collab sama operator logika
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# or / and / not 
if a > b or a > c:
    print("At least one of the conditions is True")

# nested if
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

"""
-------------------------While Loop
"""

# while -" cetak i selama i kurang dari 6"
i = 1
while i < 6:
    print(i) # kalau ditulis sampe sini doang bkl cetak angka 1 terusss
    i += 1 # tambah 1 setiap iterasi

# break -> stop loop
i = 1
while i < 6:
    print(i)
    if i == 3: # stop di angka 3
        break # stop
    i += 1 # tambah 1 setiap iterasi

# continue -> lanjutkan ke iterasi berikutnya
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue # lewati angka 3
    print(i)

# else -> eksekusi perintah baru setelah loop selesai
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


"""
-----------------------For Loop
"""

# for untuk list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# mengulangi huruf-huruf dalam kata
for x in "banana":
    print(x)

# break -> stop loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break # stop di banana, ini print baru break
# outputnya bkal keluar apple, banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x) # stop di banana, tpi kli ini break baru print
# outputnya bakal keluar apple


# continue -> lanjutkan ke iterasi berikutnya
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x) # lewati banana
# outputnya bakal keluar apple, cherry


# range() 
for x in range(6):
    print(x) # output 0 - 5

# range () -> dua parameter
for x in range(2, 6):
    print(x) # output 2 - 5

# range () -> tiga parameter
for x in range(2, 30, 3):
    print(x) # output 2, 5, 8, 11, 14, 17, 20, 23
"""
 membedah range(2, 30, 3)
    2 -> mulai dari 2
    30 -> berhenti sebelum 30
    3 -> loncat 3 angka
"""


# else
for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: break # ada break,
    print(x)
else:   # otomatis else gk di eksekusi karena dah stop di break
    print("Finally finished!")


# loop bersarang
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
# kombinasi dua output antara variabel adj dan fruits

# pass -> biarkan loop kosong
for x in [0, 1, 2]:
    pass
# outputnya bakal kosong

"""
------------------ Python function
"""

# fungsi -> blok kode yang hanya berjalan ketika di panggil

# def -> mendefinisikan fungsi
def my_function():
    print("Hello from a function")

my_function() # ini guna manggil dia


# argumen ---- biasa di singkat args
def my_function(): # dalam tanda kurung adalh parameter
    print("Hello, ")

"""
              Parameter / Argumen

Istilah parameter dan argumen dapat digunakan untuk hal yang sama: informasi yang diteruskan ke suatu fungsi.

Dari perspektif fungsi:

Parameter adalah variabel yang tercantum di dalam tanda kurung dalam definisi fungsi.

Argumen adalah nilai yang dikirim ke fungsi saat dipanggil.

"""

# jumlah argumen
def my_function(pertama, kedua): # 2 parameter
    print(pertama + " " + kedua)

my_function("alah", "masa") # juga dipanggil 2 argumen jga
# parameter = pertama dan kedua
# argumen = alah dan masa

# yg salah
def my_function(fname, lname): # dia berharap 2 argumen
  print(fname + " " + lname)

my_function("Emil") # mlh cuma satu, bakalan eror

# jika tak tahu berapa banyak argumen?  ---> *args
def my_function(*kids):  # gunakan * sebelum nama argumen
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") # argumen = emil tobias linus

# argumen = kunci   --->  argumen kata kunci
def my_function(child3, child2, child1): # biasa disingkat   kwargs
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# argumen kata kunci sembarang
def my_function(**kid): # biasa disingkat **kwargs
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# return --> nilai kembali
def my_function(x):
    return 5 * x

print(my_function(3))
# ini sama dengan ketika 3x5 = 15


# pass
def myfunction():
    pass
# sebenernya gk boleh kosong, cuma beberapa case pakai aja pass

# Positional-only parameter --> argumen hanya posisional
def my_function(x, /):  # koma dan garis miring disebut Positional-only parameter
    print(x)

my_function(3)

def hitung_luas_persegi_panjang(panjang, lebar, /):
  luas = panjang * lebar
  return luas

# Cara yang benar:
luas_persegi_panjang = hitung_luas_persegi_panjang(5, 3)

# Cara yang salah (akan menimbulkan error):
# luas_persegi_panjang = hitung_luas_persegi_panjang(lebar=3, panjang=5)

# positional only parameter agar di nilai dari panjang lanjut lebar, biar gk kebalik, sebut aja nilai prioritas

def misal(a, b, / c): # yg bkl di prioritaskan ya a -> b sedang c ntar aja atau yahh kalau kebagian
    print()



# ARGUMEN HANYA KATA KUNCI ----  Keyword only-parameter
def cetak_info(nama, *, usia=30, kota="Jakarta"): # bintang setelah nama berarti
  print("Nama:", nama)
  print("Usia:", usia)
  print("Kota:", kota)

cetak_info("Andi", usia=25)
# nama bisa diberikan secara positional atau keyword, gk harus nama=Andi langsung tulis Andi gpp
# usia dan kota adalah keyword-only, sehingga harus diberikan dengan menggunakan nama parameternya.

def hitung_luas_persegi_panjang(panjang, lebar, *, satuan="cm²"):
  luas = panjang * lebar
  print(f"Luas persegi panjang adalah {luas} {satuan}")

hitung_luas_persegi_panjang(5, 3, satuan="m²")  # Benar
# hitung_luas_persegi_panjang(5, 3, "m²")  # Salah, satuan harus diberikan dengan keyword
# Jadi, tanda bintang bukan hanya "tanda" dari parameter keyword-only, tetapi lebih berfungsi sebagai pemisah antara parameter positional dan keyword-only.



# GABUNGAN POSTITIONAL DAN KEYWORD --------------------------------------------
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


# REKURSIF ------- MEMANGGIL DIRINYA SENDIRI
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

"""
penjelasan nya

diketahui k = 6

tri_recursion(6)
  = 6 + tri_recursion(6-1 = 5)
  5 memanggil dirinya sendiri pada baris selanjutnya
  = 6 + 5 + tri_recursion(5-1 = 4)
  4 memanggil dirinya sendiri pada baris selanjutnya
  = 6 + 5 + 4 + tri_recursion(4-1 = 3)
  3 memanggil dirinya sendiri pada baris selanjutnya
  = 6 + 5 + 4 + 3 + tri_recursion(3-1 = 2)
  2 memanggil dirinya sendiri pada baris selanjutnya
  = 6 + 5 + 4 + 3 + 2 + tri_recursion(2-1 = 1)
  1 memanggil dirinya sendiri pada baris selanjutnya
  = 6 + 5 + 4 + 3 + 2 + tri_recursion(1-1 = 0) STOPP perintahnya gtu
  = 6 + 5 + 4 + 3 + 2 + 1
  = 21

  lha di konsol hasilnya gini

  Recursion Example Results:
1       tri_recursion(1)  1 + 0 = 1
3       tri_recursion(2)  2 + 1 = 3
6       tri_recursion(3)  3 + 2 = 5
10      tri_recursion(4)  5 + 4 = 10
15      tri_recursion(5)  10 + 5 = 15
21      tri_recursion(6)  15 + 6 = 21

Anda bisa membayangkan proses ini seperti sebuah pohon terbalik, di mana setiap cabang mewakili sebuah panggilan fungsi. Cabang-cabang ini terus bercabang hingga mencapai daun (kondisi dasar), lalu nilai-nilai dari daun dijumlahkan kembali ke atas.

jadi 1 3 6 10 ... adalah hasil percabangan dari urutan 1 - 6
"""



"""
--------------------------------FUNGSI LAMBDA --------
"""
# fungsi Lambda -> fungsi sederhana, satu baris
# fungsi Def -> fungsi struktur kompleks

# Lambda untuk menggandakan angka
double_lambda = lambda x: x * 2

# Fungsi def untuk menggandakan angka
def double_def(x):
    return x * 2

"""
----> Rumus penggunaan Lambda

Lambda argumen1, argumen 2 : .... ekspresi

"""
# contoh lambda dalam penggunaanya
# Fungsi lambda untuk menggandakan sebuah angka
double = lambda x: x * 2
print(double(5))  # Output: 10

# Fungsi lambda untuk menambahkan dua angka
tambah = lambda x, y: x + y
print(tambah(3, 4))  # Output: 7

# Fungsi lambda untuk mengurutkan list berdasarkan elemen kedua
data = [(1, 3), (2, 1), (4, 5)]
data.sort(key=lambda x: x[1])
print(data)  # Output: [(2, 1), (1, 3), (4, 5)]




"""
--------------------------ARRAY-----------
"""

# Array -> kumpulan nilai yang memiliki nomor indeks
nilai_ujian = [80, 95, 72, 88, 90]
# nilai ujian -> variabel
# 80, 95, 72 ... -> nilai array yang sudah punya no. indeks
nilai_pertama = nilai_ujian[0]  # Mengakses nilai pertama (indeks 0)
nilai_ujian[2] = 85  # Mengubah nilai pada indeks 2
nilai_ujian.append(92)  # Menambahkan nilai 92 ke akhir array
nilai_ujian.pop(1)  # Menghapus elemen pada indeks 1


"""
--------------------------- CLASS and OBJECT ------------------
"""

# class -> sistem/blue print sebuah program 
# object -> wujud fisik/ boneka yang digerakan

# class ............
class Mobil:
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun

    def start(self):
        print("Mobil dinyalakan")

    def berhenti(self):
        print("Mobil berhenti")

# object ..........
mobil_saya = Mobil("Toyota", "Corolla", 2020)

# mengakses keduanya
print(mobil_saya.merek)  # Output: Toyota
mobil_saya.start()  # Output: Mobil dinyalakan


# __init__ adalah metode khusus yang disebut constructor, digunakan untuk menginisialisasi objek saat dibuat.
# (self.....) -> referensi ke instansi kelas saat ini, digunakan untuk  mengakses variabel yg termasuk dlm kelas. nama bisa dirubah ..
class Person:
  def __init__(mysillyobject, name, age): # self berubah jadi mysillyobject
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc): # self jadi abc
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
# self ini bisa diganti  dengan nama lain, yg penting dia ada di no 1 dlm kurung

#_str_ -> ketika objek punya nilai string, pakai ini biar mudah di representasikan
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self): # perlu pakai _str_
    return f"{self.name}({self.age})"

p1 = Person("John", 36) # objek dgn nilai string

print(p1)

#_repr_ -> sama kek _str_ cuma dia lebih mudah dibaca oleh mesin karena sintaksisnya lebih rinci, sedang _str_lebih mudah dibca olh kita human
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self):
        return f"Titik pada koordinat ({self.x}, {self.y})"

# Membuat objek
point = Point(3, 4)

# Mencetak objek
print(point)  # Output: Titik pada koordinat (3, 4)
print(repr(point))  # Output: Point(x=3, y=4)

# tambahan lah.....
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self): # ini fungsi yag dimiliki oleh objek trsb
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40 # ubah age dari objek jadi 40
del p1.age # ini buat hapus objek p1
del p1 # buat hapus objek p1

print(p1.age)



"""
--------------------------- PEWARISAN / INHERITANCE ----------
"""

# kelas induk -> superclass yang mewarisi sifat ke anak
# kelas anak -> subclass yang diwarisi
class Hewan: # kelas induk
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print("Hewan ini bersuara...")

class Anjing(Hewan): # kelas anak
    def bersuara(self):
        print("Woof!")

class Kucing(Hewan): # kelas anak juga
    def bersuara(self):
        print("Meow!")

# Membuat objek
anjing = Anjing("Rex")
kucing = Kucing("Mia")

# Memanggil metode
anjing.bersuara()  # Output: Woof!
kucing.bersuara()  # Output: Meow!
"""
Kelas Induk (Hewan):

Memiliki atribut nama untuk menyimpan nama hewan.
Memiliki metode bersuara() yang mencetak pesan generik.
Kelas Anak (Anjing, Kucing):

Mewarisi semua atribut dan metode dari kelas Hewan.
Meng-override/ menulis ulang/mengganti metode bersuara() untuk memberikan perilaku yang spesifik untuk masing-masing kelas.

--
Dalam contoh di atas:

Metode bersuara() pada kelas Hewan adalah implementasi dasar.
Metode bersuara() pada kelas Anjing dan Kucing adalah override dari metode yang sama pada kelas Hewan.
"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) # super()
# fungsi super -> membuat anak mewarisi semua metode dan properti induk
    self.graduationyear = 2019 # menambahkan properti

  def welcome(self): # tambahkan metode
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen")
x.printname()

# tahukan beda properti dan metode? okeii

"""
--------------------- ITERATORS/ ITERATOR ------------
"""

# perulangan ,loop, for .. -> mengontrol aliran
# Iterator -> mengakses data secara urut

# Perulangan menggunakan for loop
numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)

# Menggunakan iterator
numbers_iter = iter(numbers)
print(next(numbers_iter))  # Output: 1
print(next(numbers_iter))  # Output: 2

# apa saja yang digunakan pada iterator?

# DAFTAR, TUPLE, KAMUS DAN SET
sim = ("apa", "sih", "lo", "masa")
myiterator = iter(sim) # metode utk dapat iteartor

print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))

# STRING
sek = "APAAAN DAH"
lah = iter(sek)

print(next(lah))
print(next(lah))
print(next(lah))
print(next(lah))
print(next(lah))
print(next(lah))
print(next(lah))
print(next(lah))
print(next(lah))
print(next(lah))

# Membuat class berupa iterator
class Angka:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myangka = Angka()
myiterlhoo = iter(myangka)

print(next(myiterlhoo))
print(next(myiterlhoo))
print(next(myiterlhoo))
print(next(myiterlhoo))
print(next(myiterlhoo)) # tapi  ini bisa gk berhenti looping lhoo klo kamu trus kasih dia next next next gtuuu..

# pakai stopiteration
class hahah:
    def __iter__(self): # __iter__ sma kek _init_ krlbh yap
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration # jadi pake ini biar berhenti..

Hahu = hahah()
iterais = iter(Hahu)

for x in iterais:
    print(x)

"""
bedanya iterasi dan perulangan

iterasi bakalan trus kasih output klo kamu kasih dia
print(next(....))
print(next(....))
print(next(....))
print(next(....))
print(next(....))
pdhl kmu cuma suruh dia nulis 2 doang, tapi... gra gra next nya masih ya print truss loss

perulangan lebih bisa dikendalikan sesuai yang kita mau
misal cuma sampe 10 ya cukup.... gtu 
"""


"""
---------------------------BANYAK BENTUK / POLIMOFIRSME ---------
"""
# misal ada kelas induk hewan -> subclas anjing dan ayam. kita pakai metode bersuara -> kita akses bersuara tapi anjing sama ayam kan suaranya beda... yupp itulah polimofirsme
# sama pake metode bersuara cuma outputnya tergantung sama objeknya...
class Hewan:
    def bersuara(self):
        pass

class Anjing(Hewan):
    def bersuara(self):
        print("Woof!")

class Kucing(Hewan):
    def bersuara(self):
        print("Meow!")

# Membuat objek
anjing = Anjing()
kucing = Kucing()

# Memanggil metode bersuara()
anjing.bersuara()  # Output: Woof!
kucing.bersuara()  # Output: Meow!

# POLIMOFIRSME KELAS
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

# PEWARISAN POLIMOFIRSME KELAS
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

"""
-------------------RUANG LINGKKUP / SCOPE
"""
# suatu variabel hanya tersedia dalam satu lokal saja

# LOCAL SCOPPEEE
def myfunc():
  x = 300 # local scope variabel -> cuma bisa digunakan disini doang
  print(x)

myfunc()

# FUNGSI DALAM FUNGSI
def myfunc(): # Ini fungsi IBU...
  x = 300 # ini variabel punya nya fungsi IBU..
  def myinnerfunc(): # eh ada fungsi ANAK, dia bisa pake varb IBU..
    print(x)
  myinnerfunc()

myfunc()

# GLOBAL SCOPE
x = 300 # ini Global scope varb, bisa diakses siapapun

def myfunc():
  print(x)

myfunc()

print(x)

# PENAMAAN VARIABEL
x = 300 # eh.. varb sama namanya

def myfunc():
    x = 200 # sa,a tuhh
    print(x)

myfunc()

print(x) # outputnya bkal 2 nanti 300 dan 200 wlupun nama sama

# KATA KUNCI GLOBAL
def myfunc():
    global x # terjebak di lokal tpi pengen go internasional? gk masalah ada
    x = 300
 # ini artinya varb x bisa diakses global
myfunc()

print(x)

# NON LOCAL
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

"""
---------------------- MODUL PYTHON --------
"""

# modul = pustaka kode
import EmptyCase # artinya akses file python eksternal di EmptyCase.py
import EmptyCase as EC # dia pake nma alias yaitu EC

a = EmptyCase.person["hub"]

print(a)

# MODUL BAWAAN PYTHON
import platform as pm

x =  pm.system()
print(x)

# dir() -> pengen tau isi modulnya apa aja
import platform

x = dir(platform) # bisa dipake disemua modul
print(x)

# MISALLLL 2 bwah ini di modul dile apelah.py
# cuma mau akses yg person1 aja, gman doungs?
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from apelah import person1

print(person1["age"])

"""
------------------------JSON - JavaScript Object Notation------------
"""

# JSON -> bhasa universal komputer, untuk menukar data antar sistem yang berbeda

# PAKET BAWAAN JSON DALAM PYTHON
import json 

# KONVERSI JSON KE PYTHON
# ini JSON
x = '{ "name":"mamat", "umur":"30", "kota":"yunani"}'

y = json.loads(x) # metode untuk konversi json ke py

print(y["umur"])


# KONVERSI PYTHON KE JSON
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x) # pYTHON KE JSON

print(y)

print(json.dumps({"name": "John", "age": 30})) # kamus
print(json.dumps(["apple", "bananas"])) # daftar
print(json.dumps(("apple", "bananas"))) # tuple
print(json.dumps("hello")) # string
print(json.dumps(42)) # int
print(json.dumps(31.76)) # float
print(json.dumps(True)) 
print(json.dumps(False))
print(json.dumps(None))


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(".", "="))) # indent utk identasi/spasi pda output
# separators -> utk mengubah pemisah default
print(json.dumps(x, indent=4, sort_keys=True)) # sort keys -> utk mengurutkan output, ya atau tidak



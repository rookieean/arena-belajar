"""
------------------------------ Numpy Present ------------------------------

Numpy adalah pustaka python
numpy digunakan untuk bekerja dgn array 
numpy -> Numerical Python


NumPy adalah pustaka Python yang digunakan untuk bekerja dengan array.

Ia juga memiliki fungsi untuk bekerja dalam domain aljabar linear, transformasi Fourier, dan matriks.

NumPy diciptakan pada tahun 2005 oleh Travis Oliphant. Ini adalah proyek sumber terbuka dan Anda dapat menggunakannya secara bebas.

NumPy adalah singkatan dari Numerical Python.

NumPy bertujuan untuk menyediakan objek array yang 50x lebih cepat daripada daftar Python tradisional.

Objek array dalam NumPy disebut ndarray, ia menyediakan banyak fungsi pendukung yang membuat pekerjaannya ndarraysangat mudah.

"""

# instal numpy
# buka cmd ketik -> pip install numpy

# periksa versi numpy
import numpy as np
print(np.__version__)



# membuat array
import numpy as np

# Membuat array 1 dimensi
arr1 = np.array([1, 2, 3, 4, 5])

# Membuat array 2 dimensi
arr2 = np.array([[1, 2, 3], [4, 5, 6]])



# operasi aritmatika
# Penjumlahan
arr1 + 5

# Perkalian
arr1 * 2

# Fungsi matematika
np.sin(arr1)



# aljabar linier
# Perkalian matriks
np.dot(arr2, arr2.T)  # arr2.T adalah transpose dari arr2

# Invers matriks
np.linalg.inv(arr2)


# Transformasi Fourier
# Menghitung DFT
np.fft.fft(arr1)



# bilangan acak
# Menghasilkan bilangan acak antara 0 dan 1
np.random.rand(5)

# Menghasilkan bilangan acak dari distribusi normal
np.random.randn(3, 3)



# objek array dlm numpy disebut ndarray
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))


# dimensi array -> berapa banyak kedalaman array

# 0-D array
import numpy as np

arr = np.array(42)

print(arr)

# contoh dari gemini ai yups......
import numpy as np

# Array 1D
array_1d = np.array([1, 2, 3, 4, 5])

# Array 2D
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Array 3D
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Mengakses elemen
print(array_1d[2])  # Output: 3
print(array_2d[1][2])  # Output: 6
print(array_3d[0][1][0])  # Output: 3

"""
pengertian mengapa outputnya bisa 3 6 3

array_1d[2] menghasilkan elemen ketiga dari array 1D, yaitu 3.

array_2d[1][2] artinya akses baris indeks ke 1 -> yang nomor indeksnya 2 

[[1, 2, 3], -> baris indeks ke-0
 [4, 5, 6], -> baris indeks ke-1
 [7, 8, 9]] -> baris indeks ke-2
 
[4, 5, 6] ini kan baris indeks ke 1, yang nomor
 0  1  2  yg nomor 2 adalah 6


 array_3d[0][1][0] artinya akses

 [[[1, 2], [3, 4]], -> halaman indeks ke-0
 [[5, 6], [7, 8]]]  -> halaman indeks ke-1

 [1, 2], [3, 4] -> yg indeks 1 adalah [3, 4]
    0       1     diket indeksnya

[3, 4] akses yg 0 brti 3 lah
 0  1 indeksnya...

"""

# periksa jumlah dimensi?
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim) # output 0
print(b.ndim) # output 1
print(c.ndim) # output 2
print(d.ndim) # output 3
# pake ndim untuk mengetahui jumlah dimensi array

# array dimensi lebih tinggi
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)
# tbh, dia satu dimensi but karena pake ndmin=5 jadi dia 5 dimensi

print(arr)
print('number of dimensions :', arr.ndim)


"""
------------------------ Numpy Array Indexing -----------------------------
"""

# MENGAKSES ELEMEN ARRAY
import numpy as np

lihat = np.array([1, 2, 3, 4, 5])

print(arr[0]) # output 1

# AKSES ARRAY 2D
import numpy as np

arred = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('2nd element', arr[0, 1]) # output 2

# AKSES ARRAY 3D
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2]) # output 6

# NEGATIF INDEXING -> mengakses elemen dari akhir array
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('Last element from 2nd dim: ', arr[1, -1]) # output 10


"""
---------------------------- Numpy Array Slicing ---------------------------
"""

# PEMOTONGAN ARRAY
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) # output 2, 3, 4, 5
print(arr[4:]) # output 5, 6, 7
print(arr[:4]) # output 1, 2, 3, 4

# PENGIRISAN NEGATIF
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1]) # output 5, 6

# MELANGKAH
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2]) # output 2, 5
# hitung dri indeks 1 -> 5 dgn lompatan 2
print(arr[::2]) # output 1 3 5 7

# MEMOTONG ARRAY 2D
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4]) # output 7, 8, 9
# Dari elemen kedua, potong elemen dari indeks 1 ke indeks 4 (tidak termasuk)
print(arr[0:2, 2]) # output 3, 8
# Dari kedua elemen, kembalikan indeks 2
print(arr[0:2, 1:4]) # output [[2 3 4] [7 8 9]]
# Dari kedua elemen, potong indeks 1 hingga indeks 4 (tidak disertakan), ini akan mengembalikan array 2-D


"""
---------------------------- TIPE DATA NUMPY --------------------
"""

# TIPE DATA DI PYTHON
# string -> huruf karakter
# integer -> bilangan bulat
# float -> desimal
# boolean -> biner
# complex -> 1.0 + 2.0j, 1.5 + 2.5j

# TIPE DATA DI NumPy
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - String
# U - unicode string
# V - fixed chunk of memory for other type (void)


# MEMERIKSA TIPE DATA ARRAY
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype) # output int64


# MEMBUAT ARRAY DENGAN TIPE DATA TERTENTU
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr) # output [b'1' b'2' b'3' b'4']
print(arr.dtype) # output |S1


# MENGONVERSI TIPE DATA PADA ARRAY YANG ADA
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')
# Ubah tipe data dari float ke integer dengan menggunakan 'i'nilai parameter
newarr = arr.astype(int)
# Ubah tipe data dari float ke integer dengan menggunakan intnilai parameter
newarr = arr.astype(bool)
# ubah tipe data dari float ke boolean
print(newarr)
print(newarr.dtype)


"""
---------------------------- COPY DAN VIEW ARRAY -------------------------
"""

# MENYALIN
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr) # output [42 2 3 4 5]
print(x) # output [1 2 3 4 5]

# MELIHAT
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# MEMERIKSA APAKAH ARRAY ADA DATANYA SENDIRI
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base) # output None -> tidak ada data
print(y.base) # output [1 2 3 4 5] -> ada data
# salinan memiliki data, sedang tampilan tidak
# Setiap array NumPy memiliki atribut base yang mengembalikan Nonejika array tersebut memiliki data. Jika tidak, base  atribut merujuk ke objek asli.


"""
--------------------------------- SHAPE ARRAY ------------------------------
"""

# Bentuk array -> jumlah elemen dalam setiap dimensi

# MENDAPATKAN BENTUK ARRAY
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape) # output (2, 4)
# outputnya bisa 2, 4 -> ada 2 baris dan setiap baris punya 4 kolom

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr) # output [[[[[1 2 3 4]]]]]
print('shape of array :', arr.shape) # output shape of array : (1, 1, 1, 1, 4)
# 1 1 1 1 4 -> 1 baris, 1 kolom, 1 halaman, 1 kedalaman, 4 elemen lihat arr


"""
-----------------MEMBENTUK ULANG ARRAY/ RESHAPE ARRAY -----------------
"""

# UBAH DARI 1D KE 2D
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr) # output [[ 1  2  3] [ 4  5  6] [ 7  8  9] [10 11 12]]


# UBAH DARI 1D KE 3D
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr) # output [[[ 1  2] [ 3  4] [ 5  6]] [[ 7  8] [ 9 10] [11 12]]]

# BISA GAK UBAH DALAM BENTUK APAPUN?
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8]) # 8 elemen

newarr = arr.reshape(3, 3) # 3 X 3 = 9 elemen

print(newarr) # OUTPUT ERROR

# MENGENBALIKAN SALINAN ATAU LIHAT
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base) # output [1 2 3 4 5 6 7 8]

# DIMENSI TAK DIKETAHUI
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr) # output [[[1 2] [3 4]] [[5 6] [7 8]]]
# -1 artinya kita tidak peduli berapa banyak kolom, asalkan 2 baris dan 2 kedalaman

# MERATAKAN ARRAY
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr) # output [1 2 3 4 5 6]



"""
---------------------- NUMPY ARRAY ITERASI ------------------------------
"""

# Iterasi -> menelusuri elemen satu demi satu
# MENGULANGI ARRAY 1D
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x) # output 1 2 3

# MENGULANGI ARRAY 2D
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x) # output [1 2 3] [4 5 6]

# MENGULANGI SETIAP ELEMEN SKALAR DARI ARRAY 2D
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y) # output 1 2 3 4 5 6

# ITERASI ARRAY 3D
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x) # output [[1 2 3] [4 5 6]] [[7 8 9] [10 11 12]]

# ULANGI 3D SAMPE SAKLAR
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z) # output 1 2 3 4 5 6 7 8 9 10 11 12

# ITERASI ARRAY DENGAN NDITER()
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x) # output 1 2 3 4 5 6 7 8
# nditer() adalah metode yang dapat digunakan untuk melakukan iterasi array multidimensi

# ITERASI DENGAN TIPE DATA BERBEDA
import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x) # output b'1' b'2' b'3'
# flags=['buffered'] digunakan untuk mengoptimalkan iterasi array dengan membuat buffer sementara
# Buffer -> tempat penyimpanan sementara
# op_dtypes=['S'] digunakan untuk mengubah tipe data elemen selama iterasi

# ITERASI DENGAN UKURAN LANGKAH YANG BERBEDA
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x) # output 1 3 5 7

# ITERASI TERHITUNG MENGGUNAKAN ndenumerate()
import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x) # output (0,) 1 (1,) 2 (2,) 3
# ndenumerate() adalah metode yang dapat digunakan untuk melakukan iterasi array multidimensi, dan mengembalikan indeks dari setiap elemen

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x) # output (0, 0) 1 (0, 1) 2 (0, 2) 3 (0, 3) 4 (1, 0) 5 (1, 1) 6 (1, 2) 7 (1, 3) 8

"""
------------------------ NUMPY JOIN ARRAY ------------------------------
"""
# MENGGABUNGKAN ARRAY
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr) # output [1 2 3 4 5 6]
# concatenate() -> menggabungkan array 2 atau lebih

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr) # output [[1 2 5 6] [3 4 7 8]]
# axis=1 -> menggabungkan array dalam kolom
# satu baris, satu sumbu krena dlm NumPy semua digabungkan berdasarkan sumbu

# MENGGABUNGKAN ARRAY DGN STACK
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr) # output [[1 4] [2 5] [3 6]]
# stack() -> menggabungkan array dalam baris


# MENUMPUK SEPANJANG  BARIS
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr) # output [1 2 3 4 5 6]
# hstack() -> menggabungkan array dalam baris


# MENUMPUK SEPANJANG KOLOM
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr) # output [[1 2 3] [4 5 6]]
# vstack() -> menggabungkan array dalam kolom


# MENUMPUK SEPANJANG KEDALAMAN
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr) # output [[[1 4] [2 5] [3 6]]]
# dstack() -> menggabungkan array dalam kedalaman


"""
------------------------ NUMPY SPLIT ARRAY ------------------------------
"""

# MEMISAHKAN ARRAY
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3) # 3 bagian

print(newarr) # output [array([1, 2]), array([3, 4]), array([5, 6])]

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4) # 4 bagian

print(newarr) # output [array([1, 2]), array([3, 4]), array([5]), array([6])]


# DIBAGI MENJADI ARRAY
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0]) # output [1 2]
print(newarr[1]) # output [3 4]
print(newarr[2]) # output [5 6]

# MEMISAHKAN ARRAY 2D
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr) # output [array([[1, 2], [3, 4]]), array([[5, 6], [7, 8]]), array([[ 9, 10], [11, 12]])]

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr) # output [array([[ 1], [ 4], [ 7], [10], [13], [16]]), array([[ 2], [ 5], [ 8], [11], [14], [17]]), array([[ 3], [ 6], [ 9], [12], [15], [18]])]
# hsplit() -> membagi array menjadi beberapa array sepanjang kolom
# hsplit() solusi alternatif untuk vstack() -> menggabungkan array dalam kolom

"""
---------------------------- NUMPY SEARCHING ARRAY -------------------------
"""

# MENCARI ARRAY
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4) # mencari angka 4

print(x) # output (array([3, 5, 6],)

"""
penjelasan outputnya

[1, 2, 3, 4, 5, 4, 4]
 0  1  2  3  4  5  6

angka 4 ada di indeks ke 3, 5, 6
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0) # mencari angka genap

print(x) # output (array([1, 3, 5, 7],)


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1) # mencari angka ganjil

print(x) # output (array([0, 2, 4, 6],)


# PENCARIAN DIURUTKAN
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7) # mencari angka 7

print(x) # output 1

# PENCARIAN DARI KANAN
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right') # mencari angka 7 dari kanan

print(x)# output 2


# BEBERAPA NILAI YANG DICARI
import numpy as np

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6]) # mencari angka 2, 4, 6

print(x) # output [1 2 3]
# searchsorted() -> memberitahu Anda di mana Anda harus memasukkan angka-angka baru ke dalam array yang sudah diurutkan sehingga urutannya tidak rusak
# Ia tidak benar-benar memasukkan angka-angkanya, hanya memberitahu di mana mereka seharusnya dimasukkan.

"""
------------------------ MENGURUTKAN ARRAY ------------------------------
"""

# MENGURUTKAN ARRAY
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr)) # output [0 1 2 3]
# sort() -> mengurutkan array. dia mengembalikan salinan tanpa merubah array asli

import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr)) # output ['apple' 'banana' 'cherry']


import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr)) # output [False True True]

# MENGURUTKAN ARRAY 2D
import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr)) # output [[2 3 4] [0 1 5]]

"""
-------------------- SUSUNAN ARRAY ------------------------------
"""

# MEMFILTER ARRAY
import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr) # output [41 43]
# mengapa nilai outputnya 41 43? karena True di indeks 0 dan 2


# MEMBUAT FILTER ARRAY
import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr) # output [False False True True]
print(newarr) # output [43 44]


# Membuat filter yang hanya mengembalikan elemen yang genap
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr) # output [False True False True False True False]
print(newarr) # output [2 4 6]


# MEMBUAT FILTER LANGSUNG DARI ARRAY
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr) # output [False False True True]
print(newarr) # output [43 44]

# buat array filter yang hanya mengembalikan elemen yang lebih besar dari 42
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr) # output [False True False True False True False]
print(newarr) # output [2 4 6]


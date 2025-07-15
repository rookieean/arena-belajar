"""
------------------ UFUNC ------------------
"""
# Ufunc -> fungsi universal NumPy

# Ufunc adalah "Universal Function" dan mereka adalah objek yang mewakili operasi matematika antara elemen-elemen array.

# Menggunakan Ufunc, operasi vektorisasi diimplementasikan dalam NumPy, yang memungkinkan untuk melakukan operasi yang sama pada banyak elemen dalam array dalam satu waktu.

# Ufunc adalah objek NumPy yang memungkinkan operasi aritmatika elemen demi elemen pada array.

# vektorisasi -> konsep yang memungkinkan operasi pada array secara keseluruhan, tanpa harus melakukan loop elemen per elemen.

# tanpa ufunc, bisa pake bawaan python zip:
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z) # output -> [5, 7, 9, 11]

# dengan ufunc, kita dapat menggunakan ada():
import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z) # output -> [5 7 9 11]



"""
----------------- Create Your Own Ufunc -----------------
"""

# Untuk membuat Ufunc sendiri, kita harus menerapkan fungsi Python, dan menerapkannya ke setiap elemen dalam array NumPy.
# Untuk membuat ufunc, Anda harus menambahkannya ke pustaka ufunc menggunakan fungsi tertentu yaitu frompyfunc().

# frompyfunc() -> mengambil argumen:
# function -> nama fungsinya
# inputs -> jumlah argumen masukan
# outputs -> jumlah argumen keluaran

# buat ufunc untuk penambahan:
import numpy as np

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8])) # output -> [6 8 10 12]

# Perikas apakah itu ufunc atau tidak:
import numpy as np

print(type(np.add)) # output -> <class 'numpy.ufunc'>



"""
---------------------Simple Arithmetic ---------------------
"""

# Penjumlahan:
import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr) # output -> [30 32 34 36 38 40]

# Pengurangan:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr) # output -> [-10  -1   8  17  26  35]

# Perkalian:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr) # output -> [ 200  420  660  920 1200 1500]

# Pembagian:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr) # output -> [ 3.33333333  4.          3.          5.          25.          1.81818182]


# sisa:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)

print(newarr) # output -> [1 6 3 0 0 27]
# 10 % 3 = 1 ....

# power:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr) # output -> [      1000    3200000  729000000          0     250000  1208925819614629174706176]
# 10*10* 10 = 1000....


# Hasil bagi dan mod:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr) # output -> (array([ 3,  2,  3,  5, 25,  1]), array([1, 6, 3, 0, 0, 27]))


# Absolute values:
import numpy as np

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr) # output -> [1 2 1 2 3 4]



"""
--------------------- Rounding Decimals ---------------------
"""

# pembulatan desimal -> 

# pemotongan:
# trunc() -> menghilangkan bagian desimal tanpa pembulatan
import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr) # output -> [-3.  3.]

# fix() -> menghilangkan bagian desimal tanpa pembulatan
import numpy as np

arr = np.fix([-3.1666, 3.6667])

print(arr) # output -> [-3.  3.]


# pembulatan:
# around() -> pembulatan ke desimal terdekat
import numpy as np

arr = np.around(3.1666, 2)

print(arr) # output -> 3.17

# lantai:
# floor() -> pembulatan ke bawah
import numpy as np

arr = np.floor([-3.1666, 3.6667])

print(arr) # output -> [-4.  3.]

# langit-langit:
# ceil() -> pembulatan ke atas
import numpy as np

arr = np.ceil([-3.1666, 3.6667])

print(arr) # output -> [-3.  4.]



"""
--------------------- Logs ---------------------
"""

# logaritma di pangkalan 2:
import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr)) # output -> [0.         1.         1.5849625  2.         2.32192809 2.5849625  2.80735492 3.         3.169925]


# logaritma di basis 10:
import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr)) # output -> [0.         0.30103    0.47712125 0.60205999 0.69897    0.77815125 0.84509804 0.90308999 0.95424251]


# logaritma alami atau log di dasar e:
import numpy as np

arr = np.arange(1, 10)

print(np.log(arr)) # output -> [0.         0.69314718 1.09861229 1.38629436 1.60943791 1.79175947 1.94591015 2.07944154 2.19722458]


# log di pangkalan manapun:
from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15)) # output -> 1.7005483074552052

# logaritma -> pangkat berapa sama dengan
# 2*3 = 2 x 2 x 2 = 8
# 2log 8 = 3



"""
------------------------ PENJUMPLAHAN NUMPY -------------
"""


#Tambahkan nilai dalam arr1 ke nilai dalam arr2:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr) # output -> [2 4 6]


#Jumlahkan nilai dalam arr1 dan nilai dalam arr2:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr) # output -> 12

# penjumlahan pada sumbu:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr) # output -> [6 6]

# jumlah kumulatif:
import numpy as np

arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)

print(newarr) # output -> [1 3 6]
# [1, 2, 3] adalah [1, 1+2, 1+2+3,] = [1, 3, 6,].


"""
------------------- PRODUK NUMPY ------------
"""

# Produk:
import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x) # output -> 24
# karena 1*2*3*4 = 24

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print(x) # output -> 40320
# karena 1*2*3*4*5*6*7*8 = 40320

# produk di atas sumbu:
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr) # output -> [  24 1680]
# karena 1*2*3*4 = 24 dan 5*6*7*8 = 1680

# produk kumulatif:
import numpy as np

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr) # output -> [   5   30  210 1680]
# [5, 6, 7, 8] adalah [5, 5*6, 5*6*7, 5*6*7*8] = [5, 30, 210, 1680].



"""
--------------------- PERBEDAAN NUMPY ----------------
"""

# Perbedaan:
import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr) # output -> [ 5 10 -20]
# 15-10 = 5, 25-15 = 10, 5-25 = -20


import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr, n=2)

print(newarr) # output -> [ 5 -30]
# 15-10 = 5, 25-15 = 10, 5-25 = -20
#  10-5=5 dan -20-10=-30
# dilakukan 2 kali -> n=2



"""
----------------------UFUNC MENEMUKAN KPK --------------
"""

# KPK -> Bilangan terkecil yang dapat dibagi oleh kedua bilangan tanpa sisa
import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x) # output -> 12
# 4 = 2*2
# 6 = 2*3
# 2*2*3 = 12
# 12 karena itu adalah kelipatan persekutuan terkecil dari kedua angka (4 x 3 = 12 dan 6 x 2 = 12).


# KPK di array:
import numpy as np

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x) # output -> 18
# 18 karena itulah kelipatan persekutuan terkecil dari ketiga angka (3x6=18, 6x3=18, dan 9x2=18).


import numpy as np

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x) # output -> 2520
# 2520 karena itu adalah kelipatan persekutuan terkecil dari angka 1 hingga 10.


"""
---------------------- UFUNC MENEMUKAN FPB ----------------"
"""

# FPB -> Bilangan terbesar yang dapat membagi kedua bilangan tanpa sisa
import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x) # output -> 3
# 3 karena itu adalah angka tertinggi, kedua angka tersebut dapat dibagi (6/3=2 dan 9/3=3).

# FPB di array:
import numpy as np

arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x) # output -> 4
# 4 karena itu adalah angka tertinggi, yang dapat membagi semua angka dalam array tanpa sisa.


"""
------------------------- TRIGONOMETRI UFUNC ------------------
"""

# fungsi trigonometri -> sin(), cos(), dan tan()
import numpy as np

x = np.sin(np.pi/2)

print(x) # output -> 1.0


# Menghitung sin() untuk semua elemen dalam array:
import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x) # output -> [1.         0.8660254  0.70710678 0.58778525]


# mengubah derajat menjadi radian:
import numpy as np

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x) # output -> [1.57079633 3.14159265 4.71238898 6.28318531]


# radian ke derajat:
import numpy as np

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x) # output -> [ 90. 180. 270. 360.]


# menemukan sudut:
import numpy as np

x = np.arcsin(1.0)

print(x) # output -> 1.5707963267948966


# sudut setiap nilai dalam derajat:
import numpy as np

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x) # output -> [ 1.57079633 -1.57079633  0.10016742]


# sisi miring:
import numpy as np

base = 3
perp = 4

x = np.hypot(base, perp)

print(x) # output -> 5.0
# 5.0 karena itu adalah sisi miring dari segitiga dengan sisi dasar 3 dan sisi tegak lurus 4.


"""
----------------------ufunc hiperbolik --------------
"""

# fungsi hiperbolik -> sinh(), cosh(), dan tanh()

# fungsi hiperbolik:
import numpy as np

x = np.sinh(np.pi/2)

print(x) # output -> 2.3012989023072947


# temmukan nilai cosh untuk semua nilai di  arr:
import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.cosh(arr)

print(x) # output -> [2.50917848 1.60028686 1.32460909 1.20397209]


# menemukan sudut:
import numpy as np

x = np.arcsinh(1.0)

print(x) # output -> 0.881373587019543


# sudut setiap nilai dalam array:
import numpy as np

arr = np.array([0.1, 0.2, 0.5])

x = np.arctanh(arr)

print(x) # output -> [0.10033535 0.20273255 0.54930614]


"""
-------------------- OPERASI SET NUMPY ----------------
"""

# membuat set di numpy:
import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x) # output -> [1 2 3 4 5 6 7]


# menemukan kesatuan:
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr) # output -> [1 2 3 4 5 6]

# menemukan persimpangan:
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.intersect1d(arr1, arr2, assume_unique=True)

print(newarr) # output -> [3 4]

# menemukan perbedaan:
import numpy as np

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique=True)

print(newarr) # output -> [1 2]

# menemukan perbedaan simetris:
import numpy as np

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr) # output -> [1 2 5 6]


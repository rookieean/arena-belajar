""" 
---------------- Random Numbers in NumPy
"""

# Random Number -> angka yang tidak dapat di prediksi secara logis

# hasilkan angka ancak
from numpy import random

x = random.randint(100)

print(x)

# Random Float
from numpy import random

x = random.rand()

print(x)

# hasilkan array acak
from numpy import random

x=random.randint(100, size=(5))

print(x) # output: [17  2  1  8  0] random pokoknya

from numpy import random

x = random.randint(100, size=(3, 5))

print(x) # output: [[ 3  3  7  9 19] [21 36  9  6  1] [ 1 22  0  0  6]] random pokoknya

# Mengapung
from numpy import random

x = random.rand(5)

print(x) # output: [0.111
#  0.21038256 0.02182457 0.26554666 0.49157316] random pokoknya

# Hasilkan array 2-D dengan 3 baris, setiap baris berisi 5 angka acak
from numpy import random

x = random.rand(3, 5)

print(x) # output: [[0.30220482 0.86820411 0.1654503  0.11659149 0.54323428] [0.97375552 0.66613958 0.92426513 0.50897372 0.58931289] [0.34020174 0.19803607 0.92687975 0.81362494 0.33505694]] random pokoknya

# Menghasilkan angka acak dari array
# Mengembalikan salah satu nilai dalam array
from numpy import random

x = random.choice([3, 5, 7, 9])

print(x) # output: 7 random pokoknya


# Hasilkan array 2-D yang terdiri dari nilai-nilai dalam parameter array (3, 5, 7, dan 9)
from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x) # output: [[7 5 7 7 3] [7 7 7 7 7] [
# 7 9 7 7 3]] random pokoknya

"""
------------------------- DISTRIBUSI DATA ACAK ------------
"""

# Distribusi Data Acak
# Distribusi adalah kumpulan semua kemungkinan nilai.
"""
Hasilkan array 1-D yang berisi 100 nilai, di mana setiap nilai harus 3, 5, 7 atau 9.

Peluang untuk nilai menjadi 3 ditetapkan sebesar 0,1

Probabilitas untuk nilai menjadi 5 ditetapkan sebesar 0,3

Peluang untuk nilai menjadi 7 ditetapkan sebesar 0,6

Peluang untuk nilai menjadi 9 ditetapkan menjadi 0
"""
from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x) 


# Contoh yang sama seperti di atas, tetapi mengembalikan array 2-D dengan 3 baris, masing-masing berisi 5 nilai.
from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)

"""
--------------------PERMUTASI ACAK ---------------
"""

# Permutasi adalah acak urutan dari setiap elemen dalam set.
# [1, 2, 3, 4] -> [4, 1, 3, 2]

# Acak urutan elemen array
from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr) # output: [3 2 5 1 4] random pokoknya


# Menghasilkan permutasi array
from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr)) # output: [3 1 4 5 2] random pokoknya

"""
-------------SEABORN-------------
"""

# Seaborn adalah library Python yang berfungsi untuk membuat visualisasi data yang
# menarik dan informatif. Seaborn dibangun di atas library Matplotlib dan

# Install Seaborn
# pip install seaborn 

# membuat plot distplot
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()

# membuat plot distplot tanpa histogram
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()

"""
-----------------------Distribusi Normal----------
"""

# Distribusi Normal adalah distribusi probabilitas yang simetris di sekitar rata-rata, di mana sebagian besar nilai berada dekat dengan rata-rata dan sedikit nilai yang jauh dari rata-rata.

# distribusi normal juga dikenal sebagai distribusi Gaussian karena bentuknya yang berbentuk lonceng.
from numpy import random

x = random.normal(size=(2, 3))

print(x)

# Hasilkan distribusi normal acak berukuran 2x3 dengan mean 1 dan deviasi standar 2
from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)

# loc -> mean (rata-rata)
# scale -> standar deviasi (sebaran data)
# size -> bentuk array

# Visualisasi Distribusi Normal
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show()

"""
------------------ DISTRIBUSI BINOMIAL ------------
"""

# Distribusi Binomial adalah distribusi diskrit dari sejumlah percobaan di mana setiap percobaan menghasilkan hasil positif atau negatif (sukses atau gagal).

# Diberikan 10 kali percobaan melempar koin, hasilkan 10 titik data
from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x) # output: [5 5 5 5 5 5 5 5 5 5] random pokoknya

# n -> jumlah percobaan
# p -> probabilitas setiap percobaan
# size -> jumlah hasil

# Visualisasi Distribusi Binomial
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()

"""
--------------- DISTRIBUSI POSSION -----------
"""

# Distribusi Poisson adalah distribusi diskrit yang mengukur jumlah kali peristiwa yang terjadi dalam interval waktu tertentu.
# misal ia makan dua kali sehari, berapa probabilitas ia makan 3 kali sehari

# lam -> rata-rata jumlah peristiwa yang terjadi dalam interval waktu tertentu
# size -> bentuk array

# Hasilkan distribusi acak 1x10 untuk kejadian 2
from numpy import random

x = random.poisson(lam=2, size=10)

print(x) # output: [1 2 2 2 1 2 2 1 2 2] random pokoknya

# Visualisasi Distribusi Poisson
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()

# PERBEDAAN DIST NORMAL DAN DIST POSSION
# normal -> berkelanjutan
# poisson -> diskrit 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show()

# PERBEDAAN DIST BINOMIAL DAN POSSION
# binomial -> jumlah percobaan
# poisson -> jumlah kejadian
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()

"""
Perbedaan Utama:
Distribusi Normal: Probabilitas kontinu, dengan bentuk lonceng, ditentukan oleh mean dan standar deviasi.

Distribusi Binomial: Probabilitas diskrit, menggambarkan jumlah keberhasilan dalam percobaan yang memiliki dua hasil (keberhasilan atau kegagalan), ditentukan oleh jumlah percobaan dan probabilitas keberhasilan.

Distribusi Poisson: Probabilitas diskrit, menggambarkan jumlah kejadian dalam interval tertentu, ditentukan oleh rata-rata kejadian (λ).
"""


"""
------------------------ UNIFORM DISTRIBUTION ------------
"""

# Distribusi seragam -> menggambarkan probabilitas di mana setiap kejadian memiliki peluang sama

# low -> batas bawah - default 0,0
# high -> batas atas - default 1,0
# size -> bentuk array yang di kembalikan



# buat sampel distribusi seragam 2x3
from numpy import random

x = random.uniform(size=(2, 3))

print(x) # output [[0.5488135  0.71518937 0.60276338] [0.54488318 0.4236548  0.64589411]] random pokoknya

# Visualisasi Distribusi Seragam
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000), hist=False)

plt.show()

"""
----------------------- LOGISTIC DISTRIBUTION ------------
"""

# Distribusi Logistik adalah distribusi probabilitas yang digunakan untuk menggambarkan pertumbuhan.

# loc -> mean, default 0
# scale -> standar deviasi, default 1
# size -> bentuk array yang di kembalikan

# buat sampel distribusi logistik 2x3
from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x) # output [[ 1.62434536  1.38824359  1.47182825] [ 1.86540763  1.01545392 -0.41249321]] random pokoknya

# Visualisasi Distribusi Logistik
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size=1000), hist=False)

plt.show()

# PERBEDAAN DIST LOGISTIK DAN DIST NORMAL
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show()



"""
----------------------------- MULTINOMIAL DISTRIBUTUION ----------------
"""

# Distribusi Multinomial adalah generalisasi dari distribusi binomial. Ini menggambarkan probabilitas dari observasi kategori lebih dari dua.

# n -> jumlah percobaan
# pvals -> list probabilitas untuk setiap kategori
# size -> bentuk array yang di kembalikan

# Buat conroh lemparan dadu
from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x) # output [1 1 1 1 1 1] random pokoknya


"""
------------------------ EXPONENTIAL DISTRIBUTION ----------------
"""

# Distribusi eksponensial adalah distribusi probabilitas yang menggambarkan waktu antara peristiwa dalam interval waktu.

# scale -> inverse dari laju peristiwa, default 1.0
# size -> bentuk array yang di kembalikan

# contoh dengan skala 2,0 dengan ukuran 2x3
from numpy import random

x = random.exponential(scale=2, size=(2, 3))

print(x) # output [[0.83261985 0.6786356  0.40154815] [0.89604461 0.21468485 0.04557173]] random pokoknya

# Visualisasi Distribusi Eksponensial
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size=1000), hist=False)

plt.show()

# HUBUNGAN ANTARA DIST POISSON DAN EKSPONENSIAL
# POISSON -> jumlh kemunculan suatu peristiwa dalam kurun waktu
# EKSPONENSIAL -> berkaitan dgn waktu antara peristiwa tersebut


"""
-------------------------- Chi Square Distribution ----------------
"""

# Distribusi Chi-Square adalah distribusi probabilitas yang digunakan dalam statistik. dasar memverivikasi hipotesis

# df -> derajat kebebasan, semakin tinggi semakin simetris
# size -> bentuk array yang di kembalikan

# derajat kebebasan 2 dengan ukuran 2x3
from numpy import random

x = random.chisquare(df=2, size=(2, 3))

print(x) # output [[0.51421884 0.14486599 0.18674261] [0.26977445 0.01557602 0.0136973]] random pokoknya

# Visualisasi Distribusi Chi-Square
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()

"""
------------------------- RAYLEIGH DISTRIBUTION ----------------
"""

# Distribusi Rayleigh adalah distribusi probabilitas yang digunakan dalam komunikasi nirkabel dan model teori gangguan.
# digunakan dalam pemrosesan sinyal

# scale -> skala, default 1.0
# size -> bentuk array yang di kembalikan

# contoh dengan skala 2,0 dengan ukuran 2x3
from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x) # output [[2.0732821  2.0732821  1.68207384] [1.68207384 1.68207384 1.68207384]] random pokoknya

# Visualisasi Distribusi Rayleigh
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()

# KESAMAAN DIST RAYLEIGH DAN CHI SQUARE
# pada unit stddev dan 2 derajat kebebasan , rayleigh dan chi square mewakili distribusi yang sama

"""
-----------------------PARETO DISTRIBUTION ----------------
"""

# Distribusi Pareto digunakan dalam ekonomi dan ilmu perilaku untuk mendeskripsikan alokasi kekayaan

# a -> bentuk dan default 1
# size -> bentuk array yang di kembalikan

# bentuk 2 dengan ukuran 2x3
from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x) # output [[0.10701308 0.10701308 0.10701308] [0.10701308 0.10701308 0.10701308]] random pokoknya

# Visualisasi Distribusi Pareto
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()


"""
---------------------- ZIPF DISTRIBUTION ----------------
"""

# Distribusi Zipf digunakan untuk menggambarkan data yang memiliki distribusi ekstrim

# a -> bentuk dan default 2
# size -> bentuk array yang di kembalikan

# bentuk 2 dengan ukuran 2x3
from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x) # output [[1 1 1] [1 1 1]] random pokoknya

# Visualisasi Distribusi Zipf
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()


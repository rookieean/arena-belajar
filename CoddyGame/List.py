"""
                                            LIST
"""



"""

"""

# yang saya bikin
def values(lst):
    my_list = [10, 20, 30, 40, 50]
    for i in range(len(my_list)):
        my_list[i]

# yang benar....
def values(lst):
    for i in range(len(lst)):
        print(lst[i])








# what i ve made
def sum_elements(lst):
    lst = []
    for i in range(len(lst)):
        print(lst[i])


# jawabannya yg benar
def sum_elements(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    print(total)










# LIST GANTI + Fungsi

# yang gua biki
def change_element(lst, index, new_element):
    return [lst for lst in index]


# jawabannnya
def change_element(lst, index, new_element):
    lst[index] = new_element
    return lst






"""
    ada list 1 = [1, 2, 3, 4, 5,]
    index = nomor yg mau diakses
    list2 = list lain [8, 5, 6, 3, 7, 7, 6]


    gua mau ganti list1[2] sama list2[4], caranya ya gini
    kyak gua ada dua eskrim, gua mau eskrim yg dua tambahin ke eskrim pertama, (tapi dikit aja)
"""


# yang gua bikin...
def change_element(list1, index, list2):
    list1[index] = list2
    return list1


# jawabannya...
def change_element(list1, index, list2):
    list1[index] = list2[0]
    return list1
















# yang gua bikin...
def merge(lst1, lst2):
   new_file = lst1.append(lst2)
   new_file = lst1.sort()
   return new_file



# jawabannya.....
def merge(lst1, lst2):
    res = []
    for i in range(len(lst2)):
        res.append(lst2[i]) # dihitung satu* lalu ditambahke res[]
    for i in range(len(lst1)):
        res.append(lst1[i])
    res.sort()
    return res


















# menghitung angka (dikalikan dari daftar list; lalu dijumlah)

def prod(lst):
    res = 0
    for c in str(lst):
        res = res * int(c)
    return res


def prod(lst):
    res = 1             # res isi 1
    for i in range(len(lst)):   # i dalam rentang panjang 'lst'
        res *= lst[i]           #   res (1) x setiap yg ada (i) dalam 'lst'
    return res                  # kembali lakuin ke atas lagi













# membalikan list dari belakang

def reverse(lst):
    res = []                # list kosong
    for i in range(len(lst)):       # i dalam panjang 'lst'
        res.append(lst[len(lst) - i - 1])   # res = ditambah dalam 'lst' (dalam panjang 'lst' setiap (i) dikurangi 1)
    return res













# menggabungkan list lalu di filter

def combine_and_filter(lst, threshold):
    filtered = []
    for i in range(0, len(lst)):
        if lst[i] > threshold:
            filtered.append(lst[i])
    filtered.sort()
    return filtered












# iterasi dari setiap element
lst = input().split(",")

panjang = []  # Inisialisasi list kosong untuk menyimpan kata-kata panjang

for kata in lst:        # setiap kata dalam lst (list yg ada isinya)
    if len(kata) > 5:       # jika panjang kata lebih dari 5
        panjang.append(kata)    # [kotak panjang] akan ditambah dalam kata

print(panjang)  # tampilkan output panjang
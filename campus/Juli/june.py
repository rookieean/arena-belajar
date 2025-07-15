"""
nama = ["anna", "bana", "solia"]
nama.append ("nana") # perintah untuk nambah list
nama.append ("januar")
nama.remove ("bana") # hapus list
print("jumlah data : ", len(nama)) #hitung juamlah data
nama [0] = ("gaga") # edit list
for kata in nama:
    print(kata)
"""

# buat sebuah input dari data yng berisi daftar mahasiswa baru beserta jumlahnya

"""
name_of = [
    "Adiyatma Mahavir Bagaskara"
    "Aftbah Fathian"
    "Akmal Atharrayhan"
    "Athaya Putra"
    "Bahi Dzakwan"
    "Barra Rafeyfa Zayan"
    "Bisri Deedath"
    "Caka Radhitya Irfandi"
    "Fabian Antoine Yann"
    "Fitrah Sharafat Kenzie"
    "Kafeel Hafizhan Adhitama"
    "Mashka Shofwanul"
]

# nambah list
name_of.append (input("Pamungkas Dhefin Adibrata"))
name_of.append ("Gavin Firhan Hammami")

print(name_of)

# menghapus list
name_of.remove ("Akmal Atharrayhan")

# hitung jumlah data
print("jumlah mahasiswa : ", len(name_of))

# edit list
name_of[0] = ("ucup")

for kata in name_of:
    print(kata)

jumlah_mahasiswa_baru = name_of
print("daftar mahasiswa baru : ", len(jumlah_mahasiswa_baru))
"""
            # BUAT BARU NIH..

your_student_name = input("Please Input Your Student Name : ")
your_student_name.append (input("Student Input In Your list : "))

print(input("remove action yes or no : "))

your_student_name.remove (input("masukan nama : "))


print("Amount of Students : ", len(your_student_name))
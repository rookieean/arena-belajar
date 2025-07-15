print(5*"latihan")

nilai_users = float(input("nilai users: "))

if nilai_users >= 100:
    90 >= 100
    print(f"Nilai anda A")
elif 80 >= 89:
     print(f"Nilai anda B")
elif 70 >= 79:
     print(f"Nilai anda C")
elif 60 >= 69:
     print(f"Nilai anda D")
elif 0 >= 59:
     print(f"Nilai anda F")
elif 0 >= 100:
     print(f"Nilai anda tidak ditemukan")

print(f"{nilai_users} adalah nilai anda")


# yang lain yhaa...

nilai = float(input("Masukkan nilai angka (0-100): "))

if 90 <= nilai <= 100:
    print("Nilai huruf: A")
elif 80 <= nilai < 90:
    print("Nilai huruf: B")
elif 70 <= nilai < 80:
    print("Nilai huruf: C")
elif 60 <= nilai < 70:
    print("Nilai huruf: D")
elif 0 <= nilai < 60:
    print("Nilai huruf: F")
else:
    print("Nilai tidak valid. Harus antara 0 dan 100.")
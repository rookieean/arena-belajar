"""
Buat fungsi bernama countBirdSightings yang menerima sightings sebagai parameternya. Fungsi ini menghitung berapa kali setiap jenis burung terlihat. Fungsi ini mengambil larik string yang disebut sightings, di mana setiap string mewakili jenis burung (misalnya, "robin", "blue jay"). Kembalikan kamus di mana kuncinya adalah jenis burung dan nilainya adalah hitungan. Gunakan kamus untuk melacak jumlah burung. Ulangi larik sightings, perbarui kamus untuk setiap jenis burung. Jika jenis burung tidak ada dalam kamus, tambahkan dengan hitungan 1. Jika ada, tingkatkan hitungannya sebesar 1. Parameter: sightings (daftar): Larik string yang mewakili jenis burung. Kembalikan kamus di mana kuncinya adalah jenis burung (string) dan nilainya adalah hitungan (bilangan bulat).

"""

def countBirdSightings(sightings):
    bird_counts = {}
    for bird in sightings:
        if bird in bird_counts:
            bird_counts[bird] += 1
        else:
            bird_counts[bird] = 1
    return bird_counts

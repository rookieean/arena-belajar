"""
        Buat sebuah fungsi bernama analyze_meadow yang menerima water_level dan badgerweed_present sebagai parameternya.

Seorang ilmuwan yang penasaran sedang melakukan pengukuran hidrometri di padang rumput yang subur dan dipenuhi dengan flora yang tidak biasa seperti badgerweed. Tugas Anda adalah membantu ilmuwan tersebut menentukan tindakan yang tepat berdasarkan ketinggian air dan keberadaan badgerweed.

Fungsi ini harus menggunakan operator logika dasar untuk menentukan tindakan ilmuwan dan mengembalikan pesan string terbalik.

Parameter

water_level (str): String yang mewakili ketinggian air. Bisa "tinggi", "sedang", atau "rendah" (huruf besar-kecil).
badgerweed_present (bool): Boolean yang menunjukkan apakah badgerweed ada di area tersebut.
Fungsi ini akan menentukan tindakan ilmuwan berdasarkan kondisi ini:

Jika ketinggian air "tinggi" dan terdapat gulma badgerweed: "Mempelajari flora"
Jika ketinggian air "tinggi" dan tidak ada badgerweed: "Ukur air"
Jika ketinggian air "sedang" dan terdapat badgerweed: "Ambil sampel"
Jika ketinggian air "sedang" dan tidak ada badgerweed: "Rekam data"
Jika ketinggian air "rendah" dan terdapat gulma jenis ini: "Tanaman air"
Jika ketinggian air "rendah" dan tidak ada gulma: "Jelajahi area"
Untuk ketinggian air lainnya: "Data tidak valid"
Setelah menentukan tindakan, balikkan string tindakan yang dihasilkan dan kembalikan.

Fungsi ini mengembalikan string yang mewakili pesan tindakan yang dibalik.

"""




def analyze_meadow(water_level, badgerweed_present):
    water_level == "high" or "medium" or "low" and badgerweed_present == True or False

    if water_level == "high" and badgerweed_present == True:
        print("Mempelajari Flora")
    elif water_level == "high" and badgerweed_present == False:
        print("Ukur Air")
    elif water_level == "medium" and badgerweed_present == True:
        print("Ambil sampel")
    elif water_level == "medium" and badgerweed_present == False:
        print("Rekam Data")
    elif water_level == "low" and badgerweed_present == True:
        print("Tanam Air")
    elif water_level == "low" and badgerweed_present == True:
        print("Jelajahi area")
    else:
        print("Data tidak Valid")


result = str(input("please input ur water level = "))
result2 = bool(input("there's badgerwater there? = "))

analyze_meadow(result, result2)




# jawabannya yang benar....
def analyze_meadow(water_level, badgerweed_present):
    water_level = water_level.lower()
    
    if water_level == "high":
        if badgerweed_present:
            action = "Study flora"
        else:
            action = "Measure water"
    elif water_level == "medium":
        if badgerweed_present:
            action = "Take samples"
        else:
            action = "Record data"
    elif water_level == "low":
        if badgerweed_present:
            action = "Water plants"
        else:
            action = "Explore area"
    else:
        action = "Invalid data"
    
    return action[::-1]


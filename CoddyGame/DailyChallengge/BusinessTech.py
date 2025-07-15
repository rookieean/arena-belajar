"""
Buat fungsi bernama busy_beehive yang menerima num_bees dan activities sebagai parameternya. 

Fungsi ini mensimulasikan aktivitas lebah di sarang lebah yang ramai pada sore yang cerah. Fungsi ini harus membuat "sarang lebah" yang direpresentasikan oleh daftar string, yang awalnya diisi dengan lebah yang "tidak aktif". Kemudian, fungsi ini harus mensimulasikan beberapa putaran aktivitas lebah, di mana pada setiap putaran, suatu aktivitas ditetapkan ke setiap lebah secara berurutan dari daftar aktivitas. 

Fungsi ini harus melacak berapa kali setiap aktivitas dilakukan. 
Parameter: num_bees (int): Jumlah lebah di sarang. 
Ini harus berupa bilangan bulat positif. 

activities (list): Daftar string yang merepresentasikan berbagai aktivitas lebah (misalnya, "collect_nectar", "build_comb", "feed_larvae", "guard_hive"). Fungsi ini harus melakukan langkah-langkah berikut: Buat daftar yang disebut "beehive" dengan panjang num_bees, yang awalnya diisi dengan string "tidak aktif". 

Buat kamus untuk menghitung setiap aktivitas, awalnya atur jumlah setiap aktivitas ke 0. Simulasikan 5 putaran penugasan aktivitas: Untuk setiap lebah di sarang lebah: 

Tetapkan aktivitas berikutnya dari daftar aktivitas (berputar kembali ke awal jika perlu). Perbarui status lebah di daftar sarang lebah. Tambah jumlah untuk aktivitas tersebut di kamus hitungan. 

Setelah simulasi, hitung berapa banyak lebah yang masih "diam". Buat string ringkasan yang mencakup jumlah setiap aktivitas dan jumlah lebah yang diam. Fungsi ini mengembalikan string yang meringkas aktivitas sarang lebah, mencantumkan berapa kali setiap tugas dilakukan, dan berapa banyak lebah yang masih diam.
"""
# num-bees -> jumlah lebah
# activities -> aktifitas lebah
# idle -> lebah yang naganggur

def busy_beehive(num_bees, activities):
    beehive = ["idle"] * num_bees # inisalisasi sarang lebah, variable list
    activity_count = {activity: 0 for activity in activities} # inisalisasi kamus lebah
    activity_index = 0

    for _ in range(5):  # _ karena cuma butuh rangenya doang yg berjalan
        for i in range(num_bees):
            activity = activities[activity_index % len(activities)]
            beehive[i] = activity
            activity_count[activity] += 1
            activity_index += 1

    idle_bees = beehive.count("idle")

    summary = []
    for activity, count in activity_count.items():
        summary.append(f"{activity}: {count}")
    summary.append(f"idle bees: {idle_bees}")

    return ", ".join(summary)




"""
                                PENJELASAN

Tujuan Fungsi busy_beehive
Fungsi ini mensimulasikan aktivitas lebah dalam sebuah sarang selama 5 ronde. Kita punya sejumlah lebah (num_bees) dan daftar aktivitas yang bisa mereka lakukan (activities). Fungsi ini akan menentukan aktivitas setiap lebah di setiap ronde, menghitung berapa kali setiap aktivitas dilakukan, dan berapa banyak lebah yang tetap "idle" (menganggur) pada akhirnya.




beehive = ["idle"] * num_bees: Baris ini menginisialisasi sarang lebah.

beehive: Sebuah variabel list yang akan merepresentasikan setiap lebah di sarang.
["idle"] * num_bees: Membuat list baru di mana setiap elemennya adalah string "idle". Jumlah elemen dalam list ini akan sama dengan num_bees.
Contoh: Jika num_bees adalah 3, maka beehive akan menjadi ["idle", "idle", "idle"]. Ini berarti di awal, semua lebah dalam kondisi menganggur.




activity_count = {activity: 0 for activity in activities}: Ini menginisialisasi sebuah dictionary (kamus) untuk melacak berapa kali setiap aktivitas dilakukan.

activity_count: Nama variabel dictionary.

{activity: 0 for activity in activities}: Ini adalah dictionary comprehension, cara ringkas untuk membuat dictionary. Untuk setiap activity di dalam list activities yang diberikan, sebuah key (kunci) akan dibuat dengan nama aktivitas tersebut, dan value (nilai) awalnya disetel ke 0.
Contoh: Jika activities adalah ["nectar", "pollen", "clean"], maka activity_count akan menjadi {"nectar": 0, "pollen": 0, "clean": 0}.



activity_index = 0: Ini adalah sebuah indeks yang akan kita gunakan untuk melacak aktivitas mana yang harus diberikan kepada lebah berikutnya. Ini memastikan aktivitas didistribusikan secara berurutan dari list activities.



for i in range(num_bees):: Ini adalah loop bersarang yang akan berjalan sebanyak num_bees kali di setiap ronde. Ini berarti di setiap ronde, setiap lebah akan diberi aktivitas.
i: Merepresentasikan indeks lebah saat ini (dari 0 hingga num_bees - 1).




activity = activities[activity_index % len(activities)]: Ini adalah bagian inti dari distribusi aktivitas.
len(activities): Mengembalikan jumlah total aktivitas yang tersedia.
activity_index % len(activities): Ini adalah operasi modulo. Operasi ini menghasilkan sisa pembagian activity_index dengan len(activities). Ini adalah trik umum untuk membuat indeks berulang dalam rentang tertentu.
Contoh: Jika activities adalah ["nectar", "pollen"] (panjangnya 2), dan activity_index adalah 0, maka 0 % 2 adalah 0 (aktivitas "nectar"). Jika activity_index adalah 1, maka 1 % 2 adalah 1 (aktivitas "pollen"). Jika activity_index adalah 2, maka 2 % 2 adalah 0 lagi (kembali ke "nectar"). Ini memastikan bahwa kita selalu mendapatkan indeks yang valid dari list activities dan mendistribusikan aktivitas secara bergiliran.
activities[...]: Mengambil aktivitas dari list activities berdasarkan indeks yang dihitung.




beehive[i] = activity: Menetapkan aktivitas yang baru saja dipilih ke lebah pada indeks i di dalam list beehive. Ini mengubah status lebah dari "idle" menjadi aktivitas yang spesifik.





activity_count[activity] += 1: Menaikkan hitungan untuk aktivitas yang baru saja diberikan.
activity_count[activity]: Mengakses nilai (count) dari aktivitas tertentu dalam dictionary activity_count.
+= 1: Menambahkan 1 ke nilai tersebut.




activity_index += 1: Meningkatkan activity_index untuk mempersiapkan aktivitas berikutnya bagi lebah selanjutnya.




idle_bees = beehive.count("idle"): Setelah semua 5 ronde selesai, baris ini menghitung berapa banyak lebah yang masih dalam status "idle".
beehive.count("idle"): Metode list count() mengembalikan berapa kali sebuah elemen tertentu (dalam hal ini, string "idle") muncul dalam list. Penting: Dalam implementasi ini, seharusnya tidak ada lebah yang "idle" setelah semua ronde, karena setiap lebah diberi aktivitas di setiap ronde. Jika ada lebah "idle" berarti ada bagian dari logika yang perlu diperiksa ulang atau ini memang tujuan untuk melihat apakah ada lebah yang tidak terjangkau. Dalam kasus ini, nilai idle_bees seharusnya 0.





summary = []: Menginisialisasi sebuah list kosong yang akan digunakan untuk menyimpan string ringkasan aktivitas.



for activity, count in activity_count.items():: Loop ini mengiterasi melalui setiap pasangan key-value (aktivitas dan hitungannya) di dalam dictionary activity_count.
activity_count.items(): Mengembalikan sebuah objek yang dapat diiterasi, berisi pasangan (key, value) dari dictionary.
summary.append(f"{activity}: {count}"): Menambahkan sebuah string terformat (menggunakan f-string) ke list summary. Contoh: "nectar: 15".




summary.append(f"idle bees: {idle_bees}"): Menambahkan string yang menunjukkan jumlah lebah yang menganggur ke list summary.




return ", ".join(summary): Mengembalikan hasil akhir.
", ".join(summary): Menggabungkan semua string dalam list summary menjadi satu string tunggal, dengan setiap elemen dipisahkan oleh ", ".






                        ALGORITMA SISTEM KERJA

                        
Algoritma Sistem Kerja
Inisialisasi:

Buat beehive (list) di mana semua lebah awalnya menganggur ("idle").
Buat activity_count (dictionary) di mana setiap aktivitas memiliki hitungan nol.
Setel activity_index ke nol untuk melacak aktivitas berikutnya yang akan diberikan.
Simulasi Ronde (5 Ronde):

Ulangi proses ini sebanyak 5 kali untuk mensimulasikan 5 ronde aktivitas.
Distribusi Aktivitas per Lebah:

Di setiap ronde, untuk setiap lebah di sarang (num_bees):
Pilih Aktivitas: Gunakan activity_index dengan operator modulo (%) untuk memilih aktivitas dari list activities secara bergiliran (misalnya, jika ada 3 aktivitas, lebah pertama dapatkan aktivitas 0, lebah kedua aktivitas 1, lebah ketiga aktivitas 2, lebah keempat kembali ke aktivitas 0, dan seterusnya). Ini memastikan distribusi aktivitas yang merata.
Perbarui Status Lebah: Ubah status lebah saat ini di beehive dari "idle" menjadi aktivitas yang dipilih.
Hitung Aktivitas: Tingkatkan hitungan untuk aktivitas yang dipilih di activity_count.
Lanjutkan Indeks: Tingkatkan activity_index untuk memastikan aktivitas berikutnya akan diberikan pada lebah selanjutnya.
Hitung Lebah Menganggur (Idle):

Setelah semua 5 ronde selesai, hitung berapa banyak lebah yang masih berstatus "idle" di list beehive. (Seperti yang disebutkan, dengan algoritma ini, nilai ini seharusnya 0 karena setiap lebah selalu diberi aktivitas).
Buat Ringkasan:

Bangun sebuah list string summary.
Untuk setiap aktivitas dalam activity_count, tambahkan string seperti "activity_name: count" ke summary.
Tambahkan string untuk jumlah lebah yang menganggur ke summary.
Kembalikan Hasil:

Gabungkan semua string dalam list summary menjadi satu string tunggal yang dipisahkan oleh koma dan spasi, lalu kembalikan string tersebut.
Contoh Alur Kerja
Misalkan num_bees = 2 dan activities = ["collect", "pollinate"].

Inisialisasi:

beehive = ["idle", "idle"]
activity_count = {"collect": 0, "pollinate": 0}
activity_index = 0
Ronde 1:

Lebah 0:
activity = activities[0 % 2] = activities[0] = "collect"
beehive menjadi ["collect", "idle"]
activity_count["collect"] menjadi 1
activity_index menjadi 1
Lebah 1:
activity = activities[1 % 2] = activities[1] = "pollinate"
beehive menjadi ["collect", "pollinate"]
activity_count["pollinate"] menjadi 1
activity_index menjadi 2
Ronde 2:

Lebah 0:
activity = activities[2 % 2] = activities[0] = "collect"
beehive menjadi ["collect", "pollinate"] (tetap)
activity_count["collect"] menjadi 2
activity_index menjadi 3
Lebah 1:
activity = activities[3 % 2] = activities[1] = "pollinate"
beehive menjadi ["collect", "pollinate"] (tetap)
activity_count["pollinate"] menjadi 2
activity_index menjadi 4
... dan seterusnya hingga 5 ronde selesai.

Setelah 5 Ronde:

activity_count akan menjadi {"collect": 5, "pollinate": 5} (karena ada 2 lebah * 5 ronde = 10 total aktivitas, dibagi rata 5 untuk setiap aktivitas).
beehive akan berisi aktivitas terakhir yang ditugaskan kepada setiap lebah (misalnya, ["collect", "pollinate"] lagi jika dimulai dari collect dan pollinate untuk lebah 0 dan lebah 1 di ronde terakhir).
idle_bees = beehive.count("idle") akan menghasilkan 0.
Hasil Akhir:
"collect: 5, pollinate: 5, idle bees: 0"

"""

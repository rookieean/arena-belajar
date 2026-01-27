
// fun -> deklarasi function
// main -> nama function
// println -> menampilkan pesan baris
// di kotlin tidak perlu ;

fun pertama() {
    println("Hello World!")
    print("ini print kedua")
    print("ini print ketiga")
}

/*

jika pakai println -> dia kan kasih baris baru
jika pakai print -> dia gak akan kasih baris baru

*/




// Variabel
/*

    val -> tidak bisa dirubah
    var -> bisa dirubah

*/

fun main() {
    // variabel di kotlin
    val bucketOne = "Fish"
    var bucketTwo = 180

    println(bucketOne)
    println(bucketTwo)



    // konversi ke tipe data lain
    var angka = 13
    var string = angka.toString()
    println(string)




    // if else di kotlin
    if (bucketTwo == 180) {
        println("Selamat kamu benar")
    }else {
        println("Maff ulangi lagi")
    }



    // else if kotlin
    if (bucketOne != "Tuna") {
        println("Ini bukan Tuna!")
    } else if (bucketOne == "Fish") {
        println("Ini isinya Ikan!")
    } else {
        println("Maaf gak ada yang cocok buat kamuuuu...")
    }



    // if ditaruh di variabel
    var time = 20
    var ucapan = if (time <= 20) {
        "Welcome"
    }else {
        "You'ar late!"
    }
    println(ucapan)





    // shorhand if
    val ucapanKedua = if (time < 10) "Nanas" else "Semangka"
    println(ucapanKedua)



    // concatenate in kotlin
    var namaPertama = "Jono"
    var namaTengah = "Asparin"
    println("Nama tetanggaku adalah $namaPertama $namaTengah")

}

/*
    string harus pakai " " klo ' ' dia gak mau
    program harus di taruh di { }, diluar itu dia gak mau
    dia hanya berjalan di function main() jika ada fungsi lain di gak ngejalanin
    output code akan ada di 'Output' terminal, pakai ekstensi code runner 

    klo pake $ gak perlu kuatir sama spasi deh..

    

*/


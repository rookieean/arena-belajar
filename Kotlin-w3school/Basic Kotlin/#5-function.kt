fun main() {
    
    // membuat fungsi sendiri
    fun myFunction() {
        println("Hello World")
    }

    myFunction() // panggil fungsi trsb






    // parameter dan argumen
    // di kotlin, setiap parameter harus di inisialisasi dulu nilainya
    fun fungsiKedua(nama: String, umur: Int) {
        println(nama + "Jaehope" + umur)
    }

    fungsiKedua("Jane", 49)
    fungsiKedua("Jade", 20)






    // return sebuah nilai di kotlin
    fun bucketLima(x: Int): Int {
        return(x * 5)
    }

    var hasil = bucketLima(3)
    println(hasil)


    
    // shorthand return
    fun tambahTambahan(x: Int, y: Int) = x + y

    var hasil2 = tambahTambahan(2, 3)
    println(hasil2)
}
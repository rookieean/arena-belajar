/*
    OOP

    Kelas = Motor
    Objek = honda, vario, beat

    Properti = honda memiliki merek, warna
    Fungsi = honda bisa bergerak, 

    setiap objek mewarisi sifat dari kelas
    note: namai kelas dengan huruf kapital pada awalnya
    
    */
    
    
    // ini kelas Car
    class Car {
        var brand = ""
        var model = ""
        var tahun = 0
    }





    
    // konstruktor dalam kotlin setelah () -> val name: ...
    class Motor(var namo: String, var modl: String, var thn: Int)
    




    // fungsi di dalam sebuah kelas

    class Buah(var buahSatu: String, var buahDua: String, var buahTiga: String) {
        fun sapaan() {
            println("Hei World")
        } 
    }




    
fun main() {

    // buat objek bernama c1
   val c1 = Car()

   // akses properti dan kasih nilai
   c1.brand = "Mustang"
   c1.model = "Ford"
   c1.tahun = 1999

   // cetak nilai
   println(c1.brand)
   println(c1.model)
   println(c1.tahun)






   // isi konstruktor
   val motor1 = Motor("Honda", "Japiro", 2020)
   println(motor1.namo)

   




   // memanggil fungsi kelas
   val buahIsi = Buah("Nanas", "Semangka", "Kelapa")

   println(buahIsi.buahSatu)

   buahIsi.sapaan()
   
}


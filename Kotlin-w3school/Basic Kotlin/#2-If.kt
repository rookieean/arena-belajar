fun main() {


    // when in kotlin
    val day = 5

    val result = when(day) {
        1 -> "Senin"
        2 -> "Selasa"
        3 -> "Rabu"
        4 -> "Kamis"
        5 -> "Juma't"
        6 -> "Sabtu"
        7 -> "Minggu"
        else -> "Gak ada hari yang kamu cari"
    }
    println(result)

    /*
        cara kerja when

        when akan ngeevaluasi nilai 'day' yang ternyata nilainya adalah 5 disini
        lalu 'day' di bandingkan ke setiap 'branch' yang ada, (ditulis pakai angka lalu diikuti -> dan valuenya)
        else untuk mencetak klo emg di setiap branch gak ada,
    
    */








    // while loop in kotlin
    var angka = 0
    while (angka < 10) {
        println(angka)
        angka++
    }



    // do while loop
    var sayur = 10
    do {
        println(sayur)
        sayur++
    }
    while (sayur <= 15)
}
fun main() {
    // contoh array di kotlin
    val arrayMe = arrayOf("Rabbit", "Snake", "Elephent", "Mouse")

    // cara aksesnya
    println(arrayMe[3])






    // ingin tahu panjang arraynya gimna? 
    val arrayTwo = arrayOf("Coffe", "Milk", "Tiramisu", "Blue")
    println(arrayTwo.size) // size -> untuk tahu panjang arraynya




    

    // periksa ada gak ya sesuatu yang kita cari ada di dalam array tersebut
    val arrayThree = arrayOf("Wannabe", "Girls Generation", "4 Minute")
    
    if ("4 Minute" in arrayThree) {
        println("Ada nih yang kamu cari")
    } else {
        println ("Coba lagi ya...")
    }






    // for loop di kotlin
    val bucket = arrayOf("Chicken", "Rabbit", "Duck")
    for (x in bucket) {
        println(x)
    }






    // kotlin 'range' -> mencari rentang nilai dengan 
    for (j in 'a' .. 'i') { // tanda ini -> ..
        println(j)
    }
}

fun main() {
    
    // break -> to jump out of a loop
    var i = 0
    while (i < 10) {
      println(i)
      i++
      if (i == 4) {
        break // bug in break used
      }
    }
    
    // continue -> break one iteration 
    var m = 0
    while (m < 10) {
      if (m == 4) {
        m++
        continue // here bug too
      }
      println(m)
      m++
    }

}

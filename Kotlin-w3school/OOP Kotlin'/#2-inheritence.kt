// parent class
open class parentClass {
    val x = 6
}


// child class
class childClass: parentClass() {
    fun myFunction() {
        println(x)
    }
}


fun main() {
    val myObj = childClass()
    myObj.myFunction()
}

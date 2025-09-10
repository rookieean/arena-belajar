```
            1. Class Method

            2. Public & Private Property
                kenapa perlu getter dan setter, klo bisa langsung dipakai dan diubah saja variablenya?

                public -> properti bisa diakses dari luar class
                private -> tidak bisa diakses dari luar

            3. About Class

                4 konsep dasar class
                encapsulation, inheritance, polymorphism, abstraction

                - encapsulation
                    data dan fungsi yang ada digabungkan dalam satu unit tunggal, disebut class/objek

                - inheritance
                    pewarisan sifat kepada class

                - polymorphism
                    bisa mengambil banyak bentuk, walaupun berbeda

                - abstraction
                    menyembunyikan detail implementasi kepada user, sambil hanya menampilkan fitur penting saja


```


// Class Advanced
// bisa menjalankan fungsi dalam class
class Person {
    constructor(name) {
        this.name = name
        this.age = this.randomize() //this refer ke class person, bukan ke constructor
    }
    randomize() {
        return Math.floor(Math.random(100) * 100)
    }
}
const p = new personalbar('you')
console.log(p.age) // angka random 1-100
console.log(p.randomize())






// Public and private property

class pacar {
    // tanda pagar menandakan relationship adlh private
    #relationship
    constructor(name, age) {
        // tanpa tanda pagar brti public
        this.name = name
        this.age = age
        this.#relationship = 'In shambes'
    }
    get getRelationship() {
        return this.#relationship
    }
    getRelation() {
        return this.#relationship
    }
}
const person = new person('you', 7200)
console.log(person.getRelationship) // 'in shambes'
console.log(person.getRelation()) // 'in shambes'
// apabila mencoba mengakses secara langsung
console.log(pacar.#relationship) // private field
console.log(pacar.relationship) // undefined
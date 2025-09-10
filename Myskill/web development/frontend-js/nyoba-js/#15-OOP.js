```
        Paradigma yang berorientasi object

        1. Constructor Function
            sebuah cara membuat func objek baru

        2. This Function
            this.
            mereferensikan variable

        3. Class Instructor
            this dan class, dengan tujuan agar keduanya lebih mudah digunakan, secara visual akan lebih rapi
            
```
// example 1 orang objek
const person1 = {
    name: 'Budi',
    umur: 13,
};



// constructor func example
function person5(nam, ag) {
    this.name = nam,
    this.age = ag // ini this
};

const person2 = new person5("zaky", 29)
console.log(person2.nam);




// constructor
class hewan {
    constructor() {
        this.namaHewan = 'Babi',
        this.makanHewan = 'Karnifora'
    };
};


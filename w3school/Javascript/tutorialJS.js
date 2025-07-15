/* 

    JavaScript 

<script>
    // code js ditulis disini
<script>

*/





/* ----------------------- Variabel JavaScript ---------------------- */

var x = 5; // angka untuk variabel global 
let y = 6; // angka untuk variabel lokal
const z = 7; // angka untuk variabel konstan


{
    var x = 12; 
}
// var x = 12; bisa diakses disini

{
    let y = 13;
}
// let y = 13; gak bisa diakses disini

// ------------ mendeklarasikan ulang variabel -------------

// let -> tidak dapat di deklarasikan ulang
// var -> dapat di deklarasikan ulang

// menggunakan var:
var x = 10;
// Here x is 10

{
var x = 2;
// Here x is 2
}

// Here x is 2


//menggunakan let:
let x = 10;
// Here x is 10

{
let x = 2;
// Here x is 2
}

// Here x is 10




// ---------------------------- const --------------------------

// const -> tidak dapat di deklarasikan ulang
const PI = 3.141592653589793;
PI = 3.14;      // This will give an error
PI = PI + 10;   // This will also give an error

// const -> tidak dapat diubah nilainya
// const -> tidak dapat diakses diluar bloknya


// ----------- yang bisa dilakukan dengan const -----------
// You can create a constant array:
const cars = ["Saab", "Volvo", "BMW"];

// You can change an element:
cars[0] = "Toyota";

// You can add an element:
cars.push("Audi");


// merubah properti objek konstan
// You can create a const object:
const car = {type:"Fiat", model:"500", color:"white"};

// You can change a property:
car.color = "red";

// You can add a property:
car.owner = "Johnson";















/* ---------------------- Operator JavaScript ---------------------- */


// ----------------- Operator Aritmatika ------------------
// operator aritmatika -> +, -, *, /, %, ++, --
// operator penugasan -> =, +=, -=, *=, /=, %=, **=
// operator perbandingan -> ==, ===, !=, !==, >, <, >=, <=
// operator logika -> &&, ||, !
// operator bitwise -> &, |, ^, ~, <<, >>, >>>
// operator string -> +
// operator ternerary -> ? :
// operator tipe -> typeof, instanceof















/* ----------------- Tipe data JavaScript ----------------- */

// string -> "Hello World", 'Hello World', `Hello World`
// number -> 123, 12.34, 0x123, 0b1010, 0o123
// bigint -> 123n, 12.34n, 0x123n, 0b1010n, 0o123n
// boolean -> true, false
// object -> {name: "John", age: 30, city: "New York"}
// array -> [1, 2, 3, 4, 5], ["apple", "banana", "cherry"], [1, "apple", true]
// null -> null
// undefined -> undefined













/* ----------------- Fungsi JavaScript ----------------- */


function myFunction(p1, p2) {
    return p1 * p2; // Mengembalikan hasil kali dari dua parameter
}

myFunction(5, 10); // Memanggil fungsi dengan argumen 5 dan 10











/* -----------------Object JavaScript ----------------- */
// object -> kumpulan properti dan metode

//Create an Object
const person = {
    firstName:"John",
    lastName:"Doe",
    age:50, eyeColor:"blue"
  }
  
  // Try to create a copy
  const x = person;
  
  // This will change age in person:
  x.age = 10;

// dalam javascript semuanya adalah object, kecuali primitif yaitu string, number, boolean, null, undefined, symbol, bigint



// JS Object Properties:
// property objek -> komponen dari objek


const orang = {
    namaDepan: "Nanda",
    namaBelakang: "Engka",
    umur: 20,

}
// cara mengakses property objek
let umur = person.age; // menggunakan dot notation
// let umur = person["age"]; // menggunakan bracket notation
// let umur = person[x]; // menggunakan bracket notation dengan variabel

// menghapus property objek
delete orang.umur;
// menambahkan property objek
orang.negara = "indonee";


// objek dalam objek
myObj = {
    name: "John",
    age: 30,
    myCars: {       // objek dalam objek
        car1: "Ford",
        car2: "BMW",
        car3: "Fiat"
    }
}

// cara akses  objek bersarang
myObj.myCars.car2; // bisa cara ini
myObj.myCars["car2"]; // atau cara ini
myObj["myCars"]["car2"]; // atau cara ini











// ---------------------------- metode objek properti 

// properti -> bagian dari objek itu

// mengakses properti objek
let age = person.age; // namaObjek.properti
let age = person["age"] // namaObjek["properti"]
let age = person[x]; // namaObjek[ekspresi]



// menambahkan properti  baru
person.nationally = "English"; // namaObjek.propertiBaru = "isinya"


// menghapus properti objek
delete person.age; // menghapus objek di properti age : artinya
delete person["age"]; // cara lain


// objek bersarang
objekku = {
    nama = "tana",
    umur = 29 ,
    rumah {
        rumah1 = "menteng",
        rumah2 = "bojonegoro",
        rumah3 = "purwokerto"
    }
}

// cara akses objek bersarang
objekku.rumah.rumah3;
objekku.rumah["rumah3"]
objekku["rumah"]["rumah3"]











// ------------------------------------------ METODE OBJEK JS

// Metode -> fungsi yg ada didalam properti
// contoh....
const jeneng = {
    namaNgarep: "Bambang",
    namaBuri: "Tono",
    id : 77777,
    namaLengkap: function(){
        return this.namaNgarep + " " + this.namaBuri;  // iki metodene
    }
};


// mengakses metode objek
// namaObjek.namaMetode()
nama = jeneng.namaLengkap();


// menambahkan metode ke objek
jeneng.rumah = function(){
    return this.namaNgarep + " " + this.namaBuri;
};












// ------------------------------------ Tampilan OBJEK JS 
// OUTPUT nya akan [object object]


const harimau = {
    namaHarimau: "sumatra",
    umurHarimau: 2000,
    kota = "medan"
};

document.getElementById("demo").innerHTML = harimau; // outputnya [object object]
document.getElementById("demo").innerHTML = harimau.namaHarimau + "," + harimau.umurHarimau;
// atas itu menampilkan properti objek



// menampilkan properti dalam satu garis 
let text = "";
for (let x in harimau) {
    text += harimau[x] + " ";
};

document.getElementById("demo").innerHTML = text;
// outputnya 





























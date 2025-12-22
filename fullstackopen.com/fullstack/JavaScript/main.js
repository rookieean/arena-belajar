// const t = [1, 2, 3]

// t.push(4)
// console.log(t)

// t.forEach(value => {
//     console.log(value)
// });




// contoh 2
// const t = [1, -1, 3]

// t.push(5)

// console.log(t.length) // 4 is printed
// console.log(t[1])     // -1 is printed

// t.forEach(value => {
//   console.log(value)  // numbers 1, -1, 3, 5 are printed, each on its own line
// })       




// pakai concat
// const t = [1, -1, 3]

// const t2 = t.concat(5)  // creates new array

// console.log(t)  // [1, -1, 3] is printed
// console.log(t2) // [1, -1, 3, 5] is printed




// pakai map
const t = [1, 2, 3]

const m1 = t.map(value => value * 2)
console.log(m1)   // [2, 4, 6] is printed




// map fungsi yang lain
const m2 = t.map(value => '<li>' + value + '</li>')
console.log(m2)
// [ '<li>1</li>', '<li>2</li>', '<li>3</li>' ] is printed



// object in js
const object1 = {
    nama: 'Abna',
    umur: 28
};

console.log(object1);
console.log(object1.nama);
const fieldName = 'age';
console.log(object1[fieldName])




// arrow function
const square = (p, l) => {
    return p * l
}

const result = square(2, 9)
console.log(result)


// bisa juga pakai function
const kotak = function (p, l) {
    return p * l
}

console.log(kotak(2, 8))











// latihan pakai this pada objek
const arto = {
  name: 'Ananda Kami',
  age: 18,
  education: 'High School',
  greet: function() {
    console.log('Hello, my name is' + this.name)
  },
  doAddition: function(a, b) {
    console.log(a + b)
  },
}

arto.growOlder = function() {
  this.age += 1
}

const referenceToAddition = arto.doAddition
referenceToAddition(10, 15)
console.log(arto.name)
arto.growOlder()
console.log(arto.age)

// mengatur waktu untuk dipanggil dalam menit yang tepat
setTimeout(arto.greet, 1000)














// simulasi kelas pakai js
class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
    greet() {
        console.log('hello, my name is' + ' ' + this.name)
    }
}

const adam = new Person('Adam', 20)
adam.greet()

const jj = new Person('Asiah', 20)
jj.greet()

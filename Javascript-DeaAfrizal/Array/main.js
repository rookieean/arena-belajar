// Array

const arrayBuah = ['😊', '🧑🏻', '📃', '⚙️']

const bucket = arrayBuah.includes('📺') // apkh di array buah ada TV?
console.log(bucket)

// mencari dimana sih indexnya dari barang yang kita cari?
const posisiOrang = arrayBuah.indexOf('🧑🏻')
console.log(posisiOrang)


// mencari nilai index sebelum dan setelah
const indexBefore = posisiOrang - 1
const indexAfter = posisiOrang + 1
const before = arrayBuah[indexBefore]
const after = arrayBuah[indexAfter]

console.log(`sebelum adalah ${before}`) // bug fix. gunakan ` untuk menambahkan si before bukan pk "/'








// contoh kasus, org: sya punya array tapi gak boleh kamu ubah, klo mau pake copy dulu

const arrayBosSaya = ['🍔', '🍞', '🧂', '🌭', '🍟', '🍿']

// saya mau buat copy lalu ubah (shallow copy js/ deep copy js)
const duplikasi = [...arrayBosSaya] // cra ini bisa
const duplikasi2 = JSON.parse(JSON.stringify(arrayBosSaya)) // cara ini juga bisa

console.log({arrayBosSaya})
console.log({duplikasi})





// array bisa berisi apa aja

const arrayBisaApaAja = [
    '🧑🏻',
    {
        tomato: function() {
        console.log("ini function tomato")
    },
  },
    ['eat', 'food'],
 ]

 // memanggil function tomato beserta isinya
 arrayBisaApaAja[1].tomato








 
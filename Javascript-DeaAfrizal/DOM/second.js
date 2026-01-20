// DOM -> agar bisa mengedit element html

// ini agar kita tahu isi title apa sih..
console.log(document.title)

// cara penulisan DOM-nya
document.title

// cara ganti htmlnya
document.title = 'Samson' // title akan diganti samson

// mau edit body
document.body

/*

-> bisa pilih dari ketika opsi ini
document.textContent
document.innerHTML
document.innerText

ada perbedaan dari ketiganya...
innerHTML akan return tagHTML
innerText tidak
textContent tidak

Cara penggunaan
innerHTML -> saat ingin mengubah konten HTML
innerText -> saat cuma ingin nampilin teks aj
textContent -> mengambil semua teks tanpa peduli gaya, sprti proses data dri server

*/

// membuat elemnt baru
document.createElement














// materi pertama
document.title = 'Tenno'
const body =  document.body // biar gampang panggilnya, masukin ke variabel aj
body.append('Heiii') // append. memasukan sesuatu ke body

const h1 = document.createElement('h1') // ibrt nulis <h1></h1> di  html
h1.textContent = "Inih elementnya" // ibrt nulis "Inih elementnya" ini isi dari h1

const namaSaya = document.createElement('p')
namaSaya.innerHTML = 'Dea'

const namaKamu = document.createElement('b')
namaKamu.innerText = 'Alan'

// hasil dari h1 di munculkan di body, agar tampil
body.append(h1)
body.append(namaKamu)
body.append(namaKamu)












// materi kedua

// edit html pakai Id
const btn2 = document.getElementById('btn2')

// edit pakai class
const btn1 = document.getElementsByClassName('btn1')

// klo query selector bis dipake id, class, apa aja
const btn3 = document.querySelector('#idnya')


// cara styling html di js pakai css
btn1.style.padding = '8px'
btn1.style.margin = '8px'









// materi event listener (tiga)


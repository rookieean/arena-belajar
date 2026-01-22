const tambah = document.getElementById('btn-one');
const kurang = document.getElementById('btn-two');
const penghitungAngka = document.getElementById('kotakNilai');
let skor = 0;

function tambahAngka() {
   penghitungAngka.textContent = skor;

   if (skor > 0) penghitungAngka.style.color = "green";
   else if (skor < 0) penghitungAngka.style.color = "red";
   else penghitungAngka.style.color = "black";
};

tambah.addEventListener('click', function() {
    skor++
    tambahAngka()
});

kurang.addEventListener('click', function() {
    skor--
    tambahAngka()
});
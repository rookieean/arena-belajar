const body = document.body
const button = document.querySelector('#btn-primary')

function randomColor() {
    button.style.background = "hotpink"
}

function getRandomRgbColor() {
  // Fungsi bantu untuk mendapatkan angka acak 0-255
  const randomByte = () => Math.floor(Math.random() * 256);

  /*
  randomByte = adlh fungsi kecil, di dalamnya
  Math.floor -> akan membulatkan hasil dari Math.random
  Math.random -> akan merandom angka antar 0 - kurang dri 1 lalu di kali 256..
                angka maksimal rgb adlh 255, pke 256 agar rentangnya 0 - 255.999
  */

  // setiap angka random masukin ke variabel r g b
  const r = randomByte();
  const g = randomByte();
  const b = randomByte();

  // setiap rgb akan membentuk warna acak..
  // template literals ada `
  return `rgb(${r},${g},${b})`;

  // dgn susunan rgb(120, 230, 245) contohnya, dia kan acak terus
  
}

// masukin functionnya ke tombol di HTML
function randomButtonColor() {
    button.style.background = getRandomRgbColor()
}



// bisa jg pake cara ini
const tombol = document.querySelector('#btn-primary')

tombol.addEventListener('click', function() {
    const warnaBaru = getRandomRgbColor()

    body.style.backgroundColor = warnaBaru
});
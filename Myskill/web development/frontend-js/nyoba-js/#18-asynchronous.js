```

        Asynchronous


        js berjalan secara satu buah jalur(synchronus) untuk memproses perintah-perintah yang diberikan, istilahnya menyebutkan sebagai call stack

        simulasi pipa
        A ------------------- B

        artinya secara natural namanya synchronous,
        klo dia dikasih perintah yang banyak, dia akan baca baris perbaris.


        Asynchronous
        agar program bisa menerima banyak perintah, tanpa menunggu satu baris perintah selesai.

        js bisa menjalankan fungsi asynchronous dengan bantuan dari runtime enviroment.

        gimana caranya agar js bisa asynchronous



        Ramuan Asynchronous:

        event loop               call stack          queue stack
        handle setiap fungsi     bawaan js           bawaan browser
        masuk ke callstack




        Callback dalam Asynchronous


```

// contoh synchronous
for (let i = 0; i < 1000000; i++) {
    console.log('iterasi sedang berjalan')
}
// dia akan lag




// contoh asynchronous callback:event listener
function onButtonClick() {
    console.log('button is clicked')
}

const buttonElement = document.getElementById('button')
buttonElement.addEventListener('click', onButtonClick)



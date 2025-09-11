```

    HTTP Request & Async Await: Part 1

    Client
    mengirim permintaan request

    server
    tempat data disimpan

    proxy
    computer/tools menyampaikan pesan dari client ke server 

    caching
    menyimpan data komunikasi sementara agar proses permintaan selanjutnya

    autentikasi
    mengatur akses pada suatu data/ sumber daya sehingga hanya client tertentu yang dapat mengakses

    logging
    menyimpan/mencatat proses komunikasi




    HTTP Request

    GET
    mengambil data dari server

    POST
    mengirimkan data baru ke server

    PUT/PATCH
    mengubah data sebelumnya sudah tersedia

    DELETE
    menghapus data yang disimpan di server







    Menggunakan Fetch untuk HTTP Request

    Fetch
    merupakan seperangkat fungsional yang disediakan oleh runtime untuk melakukan request melalui HTTP.
    disediakan oleh runtime, 


    .. pake consol google dev



    Async & Await
    sebuah syntatic sugar  dari javascript agar penulisan gungsi asynchronous lebih mudah dibaca dan diekspresikan.



```

fetch(PerformanceResourceTiming, optionPost)
.then(data => data.json())
.then(data => console.log(data))
.catch(error => console.log('ada error', error))



// asyn
async function getListTodo() {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos')
    const json = await response.json()
    console.log(json)
}
```
            Callback sangat berguna dalam proses Asynchronous

            Callback Hell ( pyradmid of doom )
            kondisi dimana memiliki banyak proses yang semuanya saling bergantungan. 

            kekurangan
            jika error perlu ditangani satu persatu.





            Promise
            proxy bagi sebuah nilai yang belum dapat diketahui sebelumnya,
            memungkinkan asyn mengembalikan nilai
            

            Promise static method
            - Promise.all()
                menjalan lebih dari satu promise secara bersamaan sebagai satu promise

            - Promise.any()
                menerima argumen array of promise dan mengembalikan satu hasil promise tercepat yang berhasil

            - Promise.race()
                menerima argumen array of promise dan mengembalikan satu hasil promise tercepat



```
// promise example
function downloadImage(url) {
    return new Promise(function (resolve, reject) {
        // download sebagai contoh fungsi pengunduh yang bersifat synchronous
        const image = download(url)
        if (image) resolve(image)
        else reject('gagal mengunduh gambar: url salah')
    })
}




// static method
const promise1 = Promise.resolve(3);
const promise2 = 42;
const promise3 = new Promise((resolve, reject) => {
    setTimeout(resolve, 100, 'foo');
});

Promise.all([promise1, promise2, promise3]).then((values) => {
    console.log(values);
}); // expected output: Array [3, 42, "foo"]





// promise any

```

                EcmaScript 2
    Functional Programming & Destructive Assignment


    1. Functional Programming
        paradigma pemrograman yang didominasi oleh fungsi-fungsi

        - lebih mudah diuji dan debug (sedikit bug)
        - syntax, map filter reduce
```

// contoh bukan functional
const numbers = [1, 2, 3, 4, 5];
let totalSum = 0;
function sum() {
    for (let i = 0; i < numbers.length(); i++) {
        totalSum = totalSum + numbers[i];
        // side effect, mengubah variabel diluar fungsi
    }
}
sum();
console.log(totalSum);





// functional programming example
function sum(num) {
    const initial = 0;
    const output = num.reduce((ProgressEvent, current) => {
        console.log(prev)
        return prev + current
    }, initial);
    /**
    output dari fungsi ini hanya dipengaruhi oleh input saja
    tidak mengubah nilai apapun hanya menghasilkan nilai baru
    */
    return output;
}
const numbers2 = [1, 2, 3, 4, 5];
const total = sum(numbers2)





// filter ..... syntax
Array.filter((element, index) => {/*........... */})

const name2 = [
    { nama: 'Jane', age: 15},
    { nama: 'Lea', age: 30},
    { nama: 'Eren', age: 35},
    { nama: 'Yeager', age: 40},
    { nama: 'Zeke', age: 70},
    { nama: 'Levi', age: 25},
];

const output = name2.filter((a => a.age > 12 ));


// map ..... 
Array.filter((element, index) => {/*........... */})


//..........






// Destructuring Assignment
```
        Cara akses elemen tanpa indeks
        ana[1]

        bisa melakukan penulisan dengan lebih singkat
```

const hobi = ['surfing', 'memanjat'];
const [first, second] = hobi;
console.log(first); // surfing


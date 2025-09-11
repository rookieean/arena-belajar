```
            Callback
            merupakan fungsi (a) yang dikirimkan kepada fungsi lain (b) sebagai sebuah argumen, lalu dipanggil dalam lingkup fungsi


            Callback writting styles


```
// callback example

function greeting(name) {
    alert('Hello' + name);
}

function processUserInput(callback) { // fungsi pemanggil
    var name = prompt('Please enter your name.');
    callback(name); // si callback
}

processUserInput(greeting);





// callback writting style

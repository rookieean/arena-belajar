// Array Iteration

// forEach() call each of array one by one
const numbers = [45, 4, 9, 16, 25];

let txt = "";

numbers.forEach(myFunction);

function myFunction(value, index, array) {
    console.log(txt = value);
}



// filter() 
const bucket = [25, 9, 8, 5, 92, 28, 46]; // the bucket numbers random

const bucketFilter = bucket.filter(filterFirst);
// bucket 2, berisi bucket pertama yang difilter dengan fungsi yang hanya memilih angka lebih dari 10

function filterFirst(value, index, array) {
    return value > 10;
}










// REGEX regular expression
// use pattern to find text

//pattern/modified;
//my skill/i;

// string() bisa mencari walaupun beda huruf besar kecil no prob
let text = "Visit to Hanoi";

let nub = text.search('hanoi'); // or
let n = text.search(/hanoi/i);

// i for search case sensitive
// g perform a global match
// m perform multiline matching

let result = text.match(/is/g);
let result2 = text.match(/is/m);




// REGEX Pattern find any characters
//[abc] find any of the characters between the brackets
// [0-9] find any of the characters between the brackets
// (x|y) find any of the alternatives separated with |

let pattern = '/e/';

// regexr.com to learn bout regex


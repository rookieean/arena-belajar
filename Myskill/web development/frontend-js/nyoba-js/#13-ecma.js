// ------------------  EcmaScript 6
```
    specification regulated in ECMA-262, general use for scripting language like JavaScript

    standard language

```

// arrow function -> does not have a name
// arrow vs normal function

// arrow
const increment = x => x + 1;

// normal function
const increment2 = function(x) {
    return x + 1
}


// arrow func more than one argument
const multiply = (x, y) => x * y;
multiply(2, 2);// 4


// multiline argument using arrow func
const isCheckAge = (n) => {
    if (n <= 17) {
        return false;
    }
    return true;
}

isCheckAge(10);







// Spread Syntax mempermudah menyingkat iterable seperti string/array, gak perlu tulis satu persatu

let nub = [3, 4];
// const nub2 = [9, 5];
// i want nub2 call nub, so..
const nub2 = [9, 5, ...nub];









// fOR OF LOOP 

for (variable of iterable) {
    // code
}


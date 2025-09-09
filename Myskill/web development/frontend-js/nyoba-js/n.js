function addNumber(a, b) {
    return a + b
}

function expand(angkaPertama, angkaKedua) {
    return angkaPertama * angkaKedua
}


let result = addNumber(3, 3) + expand(addNumber, 3)

console.log(result)

// if i want to debug js in terminal, use this command
// node nameFile.js
// ofc im already install node.js for sure
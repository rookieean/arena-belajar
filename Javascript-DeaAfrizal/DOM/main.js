const btn1 = document.getElementById('btn1')
const btn = document.getElementById('button')
const body = document.body


// buttonny mengarah ke sini
function gantiWarna() {
    btn1.style.background = 'hotpink'
}

function clickButton() {
    btn1.style.background = 'aqua'
    const newText = document.createElement('p')
    newText.textContent = 'Hallo'
    body.append(newText)
}
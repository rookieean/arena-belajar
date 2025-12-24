
// A simple React component that greets a user and calculates their birth year based on age.
const Hello = ({ name, age }) => {
  const bornYear = () => new Date().getFullYear() - age

  return (
    <div>
      <p>
        Hello {name}, you are {age} years old
      </p>
      <p>So you were probably born in {bornYear()}</p>
    </div>
  )
}

const App = () => {

  return (
    <div>
      <h1>Hello</h1>
      <Hello name="Hana" age={26}/>
    </div>
  )
}











// untuk mengetahui berapa kali komponen dirender ulang
import { useState } from 'react'

const App2 = () => {
  const [ counter, setCounter ] = useState(0)

  setTimeout(
    () => setCounter(counter + 1),
    1000
  )


  console.log('rendering...', counter)

  return (
    <div>{counter}</div>
  )
}

// main.jsx nya akan terlihat seperti ini
import ReactDOM from 'react-dom/client'

import App from './App'

ReactDOM.createRoot(document.getElementById('root')).render(<App />)














// handel click untuk track brpa kli tombol bisa di klik, at keyboard/screen di click
// namanya 'event handler' 

const App3 = () => {
  const [ counter, setCounter ] = useState(0)


  const handleClick = () => {
    console.log('clicked')
  }

  return (
    <div>
      <div>{counter}</div>

      <button onClick={() => setCounter (counter + 1)}>
        tambah
      </button>

      <button onClick={() => setCounter(0)}>
        set ulang
      </button>
    </div>
  )
}


// event handler adalah fungsi atau referensi dari fungsi, mksdnya?
// jika even handler ditulis begini...
<button onClick={setCounter(counter + 1)}> 
  plus
</button>
// ini akan merusak apk itu sendiri,

// contoh even handler yang merujuk ke fungsi lain, 
const App4 = () => {
  const [ counter, setCounter ] = useState(0)


  const increaseByOne = () => setCounter(counter + 1)
  
  const setToZero = () => setCounter(0)

  return (
    <div>
      <div>{counter}</div>

        // yang merujuk ke fungsi lain
      <button onClick={increaseByOne}>
        plus
      </button>

      <button onClick={setToZero}>
        zero
      </button>
    </div>
  )
}











// 

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











// simulasi state, etc
const App5 = () => {

  // state counter -> menetapkan nilai counter
  const [ counter, setCounter ] = useState(0)
  console.log('melihat state', counter)
  
  // fungsi untuk mengubah state counter
  const increaseByOne = () =>{
    console.log('tambah di track', counter)
    setCounter(counter + 1)
  } 
  const decreaseByOne = () => setCounter(counter - 1)
  const setToZero = () => setCounter(0)

  // komponennya
  const Display = ({ counter }) => <div>{ 'penghitung mulai' + ' ' + counter}</div>
  const Button = ({ onClick, text }) => (
    <button onClick={onClick}>
      {text}
    </button>
  )

  return (
    <div>
      <Display counter={counter} />

      <Button
        onClick={increaseByOne}
        text='plus'
      />
      <Button
        onClick={setToZero}
        text='zero'
      />     
      <Button
        onClick={decreaseByOne}
        text='minus'
      />           
    </div>
  )
}













// aturan penggunaa hook, (yang udah pernah kita pelajari 'useState')
const App6 = () => {
  // these are ok
  const [age, setAge] = useState(0)
  const [name, setName] = useState('Juha Tauriainen')

  if ( age > 10 ) {
    // this does not work!
    const [foobar, setFoobar] = useState(null)
  }

  for ( let i = 0; i < age; i++ ) {
    // also this is not good
    const [rightWay, setRightWay] = useState(false)
  }

  const notGood = () => {
    // and this is also illegal
    const [x, setX] = useState(-1000)
  }

  return (
    <div>
        //...
    </div>
  )
}














// tidak menulis komponent di dalam komponent

// This is the right place to define a component
const Button = (props) => (
  <button onClick={props.onClick}>
    {props.text}
  </button>
)

const App8 = () => {
  const [value, setValue] = useState(10)

  const setToValue = newValue => {
    console.log('value now', newValue)
    setValue(newValue)
  }

  // Do not define components inside another component

  const Display = props => <div>{props.value}</div>

  return (
    <div>

      <Display value={value} />
      <Button onClick={() => setToValue(1000)} text="thousand" />
      <Button onClick={() => setToValue(0)} text="reset" />
      <Button onClick={() => setToValue(value + 1)} text="increment" />
    </div>
  )
}


// cara yang benar adlh taruh display di luar App 
const Display = props => <div>{props.value}</div>

const Button2 = (props) => (
  <button onClick={props.onClick}>
    {props.text}
  </button>
)

const App9 = () => {
  const [value, setValue] = useState(10)

  const setToValue = newValue => {
    console.log('value now', newValue)
    setValue(newValue)
  }

  return (
    <div>
      <Display value={value} />
      <Button onClick={() => setToValue(1000)} text="thousand" />
      <Button onClick={() => setToValue(0)} text="reset" />
      <Button onClick={() => setToValue(value + 1)} text="increment" />
    </div>
  )
}













// 
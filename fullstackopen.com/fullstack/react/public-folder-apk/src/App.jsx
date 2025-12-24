import { useState } from 'react'
const App = () => {

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


export default App
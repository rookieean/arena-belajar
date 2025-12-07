const App = () => {
  const now = new Date()
  const a = 10
  const b = 20
  console.log(now, a+b)

  return (
    <div>
      <p>Hello world, it is {now.toString()}</p>
      <p>
        {a} plus {b} is {a + b}
      </p>
    </div>
  )
}


// contoh props
const App2 = (props) => {
  return (
    <div>
      <p>Hello, {props.name}</p>
    </div>
  )
}

export default App2
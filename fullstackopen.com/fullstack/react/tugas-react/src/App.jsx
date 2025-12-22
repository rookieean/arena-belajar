const App = () => {
  const course = 'Half Stack Application Development'
  const parts = {
    name: 'Fundamentals of React',
    exercises: 10
  }
  const parts2 = {
    name: 'Using props to pass data',
    exercises: 7
  }
  const parts3 = {
    name: 'State of a component',
    exercises: 14
  }
  



// Header Komponent   
  const Header = () => {
    return (
      <h1>{course}</h1>
    )
  }

// Kontent Komponent
const Content = () => {
  return (
    <p>Materinya adalah {parts.name}, {parts2.name}, {parts3.name}</p>
  )
}

// Total komponent 
const Total = () => {
  return (
    <p>Total exercises: {parts.exercises + parts2.exercises + parts3.exercises}</p>
  )
}




// export isi App 
return (
  <div>
    <Header course={course} />
    <Content parts={parts} />
    <Total exercises={parts.exercises + parts2.exercises + parts3.exercises} />
  </div>
)
}

export default App
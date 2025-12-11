const App = () => {
  const course = 'Half Stack application development'
  const part1 = 'Fundamentals of React'
  const exercises1 = 10
  const partDua = 'Using props to pass data'
  const exercisesDua = 7
  const partTiga = 'State of a component'
  const exercisesTiga = 14

  // komponent Part
  const Part = () => {
    return (
      <p>{part1} {exercises1}</p>
    )
  }

  // komponent Part2
  const PartDua = () => {
    return (
      <p>{partDua} {exercisesDua}</p>
    )
  }

  // komponent Part3
  const PartTiga = () => {
    return (
      <p>{partTiga} {exercisesTiga}</p>
    )
  }

  // Komponent Content
  const Content = () => {
    return (
      <div>
        <Part part={part1} />
        <PartDua part={partDua} />
        <PartTiga part={partTiga} />
      </div>
    )
  }

  // Komponent Header
  const Header = () => {
    return (
      <h1>{course}</h1>
    )
  }


  // Komponent Total
  const Total = () => {
    return (
      <p>Number of exercises {exercises1 + exercisesDua + exercisesTiga}</p>
    )
  }



  // nampilin setiap komponent yang disusun sebelumnya
  return (
    <div>
      <Header />
      <Content />
      <Total />
    </div>
  )
}

export default App
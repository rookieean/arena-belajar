// const App = () => {
//   const now = new Date()
//   const a = 10
//   const b = 20
//   console.log(now, a+b)

//   return (
//     <div>
//       <p>Hello world, it is {now.toString()}</p>
//       <p>
//         {a} plus {b} is {a + b}
//       </p>
//     </div>
//   )
// }


// // contoh props
// const App2 = (props) => {
//   return (
//     <div>
//       <p>Hello, {props.name}</p>
//     </div>
//   )
// // }

// // export default App2



// // simulasi props kirim data ke komponent

// const Hello = (props) => {
//   console.log(props)
//   return (
//     <div>
//       <h1>
//         Hello {props.name} umurmu {props.age}
//       </h1>
//     </div>
//   )
// }

// const App = () => {
//   const name = 'Supiyah'
//   const age = 100

//   return (
//     <div>
//       <h1>Grettings</h1>
//       <Hello name='Prapto' age={23 + 10} />
//       <Hello name={name} age={age} />
//     </div>
//   )
// }

// export default App







// // komponent react harus ditulis dalam kapital, contoh...


// // komponent footer

// const footer = () => {
//   return (
//     <div>
//       greeting app created by <a href='https://github.com/mluukkai'>mluukkai</a>
//     </div>
//   )
// }


// // bagian yang nampilin

// const App2 = () => {
//   return (
//     <div>
//       <h1>Greetings</h1>
//       <Hello name='Maya' age={26 + 10} />

//       <footer /> // ini cara penulisan yang salah
//     </div>
//   )
// }






// // gini yang terjadi kalo kamu gak pake div, 

// // dia akan kasih kesalahan,
// const App3 = () => {
//   return (
//     <h1>Greetings</h1>
//     <Hello name='Maya' age={26 + 10} />
//     <Footer />
//   )
// }

// // bisa aja pakai ini
// const App4 = () => {
//   return [
//     <h1>Greetings</h1>
//     <Hello name='Maya' age={26 + 10} />
//     <Footer />
//   ]
// }

// // kurang bijak jika tanpa div, atau pakai cara ini...

// const App5 = () => {
//   const name = 'Peter'
//   const age = 10

//   return (
//     <>
//       <h1>Greetings</h1>
//       <Hello name='Maya' age={26 + 10} />
//       <Hello name={name} age={age} />
//       <Footer />
//     </>
//   )
// }



// // contoh render objek, dan pasti akan error, karena react hanya render angka dan string
// // solusinya..
// const App6 = () => {
//   const friends = [
//     { name: 'Peter', age: 4 },
//     { name: 'Maya', age: 10 },
//   ]

//   return (
//     <div>
//       <p>{friends[0]}</p>
//       <p>{friends[1]}</p>
//     </div>
//   )
// }

// // export default App6

// // solusinya..
// const App7 = () => {
//   const friends = [
//     { name: 'Peter', age: 4 },
//     { name: 'Maya', age: 10 },
//   ]

//   return (
//     <div>
//       // ditulsi seperti
//       <p>{friends[0].name} {friends[0].age}</p>
//       <p>{friends[1].name} {friends[1].age}</p>
//     </div>
//   )
// }

// // export default App


// react juga bisa render array, selama itu angka/string,
// walaupun hasilnya tidak  sesuai dengan yang kita inginkan
// const App = () => {
//   const friends = ['Peter', 'Maya']

//   return (
//     <div>
//       <p>{friends}</p>
//     </div>
//   )
// }








// latihan pakai this pada objek
const arto = {
  name: 'Ananda Kami',
  age: 18,
  education: 'High School',
  greet: function() {
    console.log('Hello, my name is' + this.name)
  },
}

arto.growOlder = function() {
  this.age += 1
}

console.log(arto.name)
arto.growOlder()
console.log(arto.age)


export default App
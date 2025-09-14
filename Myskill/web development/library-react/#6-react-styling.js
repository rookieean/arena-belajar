```
        React Lists and Styling

        1. React List
        dalam react, kita bisa me-render list dengan beberapa tipe perulangan. method map() yang disarankan untuk digunakan


        2. Key in react
        memungkinkan untuk men-tracking element dalam react. jika ada key, bisa memperbarui/menghapus item, hanya item tersebut yang perlu dirender


        3. Styling React using CSS
        - inline styling
        - camelCase  Property Name
        - javascript object



        4. CSS Stylesheet

```

// contoh react lists
function cars(props) {
    return <li> I am a {props.brand}</li>;
}

function Garage() {
    const cars = ['Ford', 'BMW', 'Audi'];
    return (
        <>
            <h1>Whoooooo</h1>
            <ul>
                {cars.map((cars) => <car brand={car} />)}
            </ul>
        </>
    );
}








// key in react
function Car(props) {
    return <li>I am a {props.brand}</li>;
}

function Garage(){
    const cars = [
        {id: 1, brand: 'Ford'},
        {id: 2, brand: 'BMW'},
        {id: 3, brand: 'Audi'},
    ];
    return (
        <>
            <h1>Who lives in my garage</h1>
            <ul>
                {cars.map((car) => <car key={car.id} brand={car.brand} />)}
            </ul>
        </>
    );
}













// styling react using css
// inline styling
const Header = () => {
    return (
        <>
            <h1 style={{color: 'red'}}>Hello Style!</h1>
            <p>Add a little style!</p>
        </>
    );
}



// camelCase Property Name
const Header2 = () => {
    return (
        <>
            <h1 style={{backgroundColor: "lightblue"}}>Hello youuu</h1>
            <p>Add a little style</p>
        </>
    );
}



// javascript object
const Header3 = () => {
    const myStle = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Sans-Serif"
    };
    return (
        <>
            <h1 style={myStle}>Hello sty</h1>
            <p>Add a little style</p>
        </>
    );
}









// CSS stylesheet -> App.js
// body {
//     backgroundColor: #282c34;
//     color: white;
//     padding: 40px;
//     fontFamily: Sans-Serif;
//     text-align: center;
// }
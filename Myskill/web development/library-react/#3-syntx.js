import { Children } from "react"

```

        JSX
        JavaScript Syntax Extension/ Javascript XML adlh ekstensi yang digunakan React



        React Element
        bagian terkecil dari sebuah aplikasi React. Digunakan untuk menyusun sebuah komponent

        JSX akan berguna ketika kode dah banyak dan rumit


        aturan penulisan JSX

        1. penempatan penulisan JSX

        class component -> dalam method render()
        functional component -> dalam statement return()
        bisa dituliskan pada variabel, dapat digunakan ulang pada komponent yang lain
        penulisan JSX untuk > 1 disarankan menggunakan tanda kurung ()


        2. penulisan atribut JSX
        atribut class perlu ditulis dengan className









        ekspresi js dalam JSX





        cara pakai react

        npx create-react-app __yang mau dibuat
        contoh:
        npx create-react-app jsx
```

// JSX
React.createElement( // fungsi createElement
    type,           // type element yang akan dibuat (string)
    [props],        // atribute untuk elemnt (object properti)
    [...Children]   // konten anak element
);




// React element
var element = React.createElement('h1', {}, 'Idonot use JSX!');





// contoh penempatan penulisan JSX

// penulisan pada class component
class Button extends React.Component {
    render() {
        <button>OK</button> // JSX
    }
}

// penulisan JSX pada sebuah variable
const CancleButton = <button>cancle</button>

// penulisan pada functional  component
function SignInButton() {
    return <button>Login</button>
}

// penulisan pada  functional component dengan arrow  function
const RegisterButton = () => <button>Register</button>








// penulisan atribut JSX
const button = <button className="btn btn-default">OK</button>;








// ekspresi js pada JSX
function myComponent() {
    return (
        <div>
            <button>{ 1 + 2 }</button>
            <button>{ Data.now() }</button>
        </div>
    );
}
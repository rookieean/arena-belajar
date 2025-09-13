```
    React adalah library JavaScript

    React Ecosystem
    - ES6+ sintaksis: const, let, class, rest parameter, spread operator, default parameter, arrow function
    - create-react-app: untuk membuat react app
    - react router: untuk mempermudah routing
    - react DOM: mengembangkan apk react pada platfrom web
    - Jest: testing framework untuk menguji mulai dari kode hingga komponent react secara lebih mudah
    - redux: state yang bersifat global



    JSX
    memungkinkan HTML ditulis langsung ke dalam JavaScript


    element
    blok bangunan terkecil di react, yang menggambarkan apa  yang akan dilihat user dilayar mereka

    elemen2
    semua element di dalam root DOM diatur oleh react DOM, untuk menampilkan react elemen pada root DOM, nanti akan dikirim ke ReactDOM.reender()

    Immutability
    react bersifat gak bisa dirubah setelah element itu dibuat, maka atribute childreennya tidak bisa diubah.




    Komponent
    function yang menerima input berupa prompt,
    klo function js akan return nilai
    klo komponent akan return react element



    Functional dan Class Component




    Props are read only


    pure function
    artinya dia tidak akan mengubah inputan function

    function sum(a, b) {    // dia gak akan ngubah a sama b
        return a + b
    }


    inpure function
    dia bisa ngubah inputan
    function withdraw(account, amount) {
        account.total -= amount;        // hasilnya berubah
    }









    
```

// JSX contoh
const element = <h1>Hello, World!</h1>



// elemen
const e = <div id="root"></div> // div adalah elemen



// elemen2
const el = <h1>Haiii</h1>
ReactDOM.render(element, document.getElementById('root'));



// functional
function welcome(props) {
    return <h1>Hello kamu!!! (props.name) </h1>
}


// class component
class welcome extends React.Component {
    render() {
        return <h1>Hello, (this.props.name) </h1>
    }
}
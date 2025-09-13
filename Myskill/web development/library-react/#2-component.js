```
        Komponent React ada 2
        1. Function
        2. Class





        Constructor
        adalah fungsi atau method khusus pada class yang akan dieksekusi saat objek dibuat atau komponent digunakan.




        State dan Props
        objek khusus yang menyimpan data untuk komponent

        state = menyimpan data ke komponent
        props = menyimpan data yang diterima dari luar komponent




        Stateful dan stateless

        stateful = komponent yang menggunakan state (container dan smart components)
        stateless = tidak menggunakan state (presentation dan dumb components)


        
```

// komponent function
function Hello() {  //  Hello, nama komponent harus huruf kapital
    return <p>Hello</p>;    // JSX
}

<Hello />   // cara menggunakan komponent


// komponent class
class Hello extends React.Component{
    render() {
        return <p>Hello</p>;
    }
}

<Hello/>




// functional component
function Header() {
    return (
        <div>
            <h1> Kalimat pertama </h1>
            <h1> Kalimat kedua </h1>
        </div>
    );
}

ReactDOM.render(<Header/>, document.getElementById("root"));






// constructor contoh
class Hello extends React.Component{
    constructor() {
        super();
        this.state = {name: "HUFTTT"};
    }

    render() {
        return <p>Hello</p>
    }
}

<Hello/>






// state dan props
this.state = {name: "my husband"}; // ini state
<komponen name="myskil" /> // ini  props


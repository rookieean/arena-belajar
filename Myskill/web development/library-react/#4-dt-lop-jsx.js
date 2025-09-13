```

        open react first

        npx create-react-app data-jsx

        cd file
        npm start = memulai react




        Displaying data in JSX
        - masuk ke App.js
        




        Perulangan di JSX
        kita tidak bisa pakai perulangan for dan while
        karena JSX hanya menjalankan ekspresi bukan statement





```

const Data = [
    {name: "Iphone", price: 10000, discount: 50}
];


// open App.js file yang akan nampilin
function App() {
    return (
        <div>
            <product>
            {Data.map((phone, id) => {
               <Product: key={id}
               name={phone.name}
               price={phone.price}
               discount={phone.discount} ></Product>
            ))}
        </div>
    )
}
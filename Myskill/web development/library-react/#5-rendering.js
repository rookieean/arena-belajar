```

        Reacts Event and Conditional Rendering

        1. add event
        ditulis dengan aturan camelCase


        2. mengirimkan argument pada event



        3. React event object




        4. Conditional Rendering


```

//  add event
{/* <button onClick=(shoot)> Take the Shot! </button>   // react
<button onClick="shoot()"> Take the Shot! </button>     // HTML */}


// menampilkan event
function Football() {
    const shoot = () => {
        alert("Great Shot!");
    }

    return (
        <button onClick={shoot}>Take the shot!</button>
    )
}






// mengirimkan argument pada event
function Foot() {
    const shoot = (a) => {
        alert(a);
    }

    return (
        <button onClick={() => shoot("Goal")}>Tka the ! </button>
    )
}





// react event object
function Fool() {
    const shoot = (a, b) => {
        alert(b.type);
    }

    return (
        <button onClick={(event) => shoot("Goal", event)}>Tkae</button>
    );                                        // click event
}













// conditional rendering
// 1. if statement

function MissedGoal() {
    return <h1>MISSED</h1>;
}

function MadeGoal() {
    return <h1>GOAL!</h1>;
}

function Goal(props) {
    const isGoal = props.isGoal;
    if (isGoal) {
        return <MadeGoal/>;
    }
    return <MissedGoal/>;
}

<Goal isGoal={false} />





// 2. Logical && operator
function Garage(props) {
    const cars = props.cars;
    return (
        <>
         <h1>Garage</h1>
            {cars.length > 0 && 
                <h2>you have {cars.length} cars in your garage.</h2>
            }
        </>
    );
}
const cars = ['ford', 'BMW', 'Audi'];
<Garage cars={cars} />





// 3. Ternary Operation

function MissedGoal() {
    return <h1>MISSED</h1>;
}

function MadeGoal() {
    return <h1>GOAL!</h1>;
}

function Goal(props) {
    const isGoal = props.isGoal;
    return (
        <>
            (isGoal ? <MadeGoal/> : <MissedGoal/>)
        </>
    );
}

<Goal isGoal={false}/>
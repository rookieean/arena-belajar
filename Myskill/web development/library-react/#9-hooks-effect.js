```
        React Hooks (useEffect)


        1. React Hooks (useEffect)
            memungkinkan untuk memberikan side effect pada components
            fetching data, directly, updating DOM dan timer

            useEffect(<function>, <dependency>)

        
        2. useEffect example on timer



        3. useEffect on Dependent Variable



```

// useeffect pada timer
import { useState, useEffect } from "react";

function Timers() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        setTimeout(() => {
            setCount((count) => count + 1 );
        }, 1000);
    });

    return <h1>I've rendered {count} times!</h1>;
}

export default Timers;






// useEffect pada dependent variable

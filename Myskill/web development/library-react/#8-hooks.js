```
            React Hooks


            1. react hooks
            memungkinkan kita untuk 'hook' ke fitur React seperti state dan lifcycle methods.


            2. Hook Rules

            - hook hanya bisa dipanggil dalam functional component react
            - hooks hanya dapat dipanggil pada top level of the component
            - hooks tidak bisa conditional

            'hooks tidak akan berfungsi pada class component react



            3. React useState Hook

            - memungkinkan untuk melacak state dalam functional component


                1. import useState
                    import { useState } from "react";
                useState menerima keadaan awal dan mengembalikan dua nilai

                2. read state

                3. update state



            
            4. Changing Object and Array State

```

// useState
function FavoriteColor() {
    const [color, setColor] = useState("");
}


// read state
import { useState } from "react";
function FavoriteColor() {
    const [color, setColor] = useState("red");

    return (
        <>
        <h1>My Favorite Color is {color} </h1>

        // update state
        <button
            type="button"
            onClick={() => setColor("blue")}
            >Blue</button>
    </>
    );
}

export default FavoriteColor;



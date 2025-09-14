```
            React Forms


            1. add from in react



            2. Handling froms

            bagaimana menangani data saat dikirimkan

            di HTML ditangani  oleh DOM
            di react ditangani  oleh component

            ketika ditangani oleh component, semua data disimpan dalam state component.




            3. submitting forms


            4. Multiple Input Fields
            
            kita dapat mengontrol nilai lebih  dari satu bidang input dengan menambahkan atribute name ke setiap element




            5. textarea
            disimpan dalam atribute value



            6. select



            7. making selected froms
            


```

// form

import React, { useState } from "react";

function MyFrom() {
    return (
        <form>
            <label>enter your name
                <input type='text'/>
            </label>
        </form>
    )
}

export default MyFrom;






// handling forms
function Myfrom() {
    const [name, setName] = useState("");

    return (
        <form>
            <label> Enter your name:
                <input type="text"
                value={name}
                obChange={(e) => setName(e.target.value)}
                />
            </label>
        </form>
    )
}







// submitting
const handleSubmit = (event) => {
    event.preventDefault();
    alert('The name you entered was: $(name)')
}

<input type="submit"/>






// multiple input fields
function my() {
    const [input, setInputs] = useState({});

    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values, [name]: value}))
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(inputs);
    }
}







// text area react
<textarea>
    isi textarea
</textarea>


const [textarea, setTextArea] = useState (
    "ini content sementara"
);

const handleChange = {event} => {
    setTextArea(event.target.value)
}

return (
    <from>
        <textarea value={textarea} onChange={handleChange}/>
    </from>
)












// select dalam react
<select>
    <option value="nana">nana</option>
    <option value="luna" selected>luna</option>
    <option value="bana">bana</option>
</select>
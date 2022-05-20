import React from 'react'
import './Button.css'
import { BrowserRouter as useNavigate} from "react-router-dom"


export default function(){
    const handleClick = () =>{
        console.log("Hello World");
    }

    return(
        <div style = {{"fontSize":50}}> 
            <div className = 'Btn'>
                <div className = 'Btn'>
                    <button onClick = {handleClick}> Third Choice</button>
                </div>
            </div>
        </div>
    )
}

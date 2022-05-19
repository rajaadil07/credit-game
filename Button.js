import React from 'react'
import './Button.css'

export default function(){
    const handleClick = () =>{
        console.log("Hello World");
    }
    return(
        <div style = {{"fontSize":50}}> 
            <div className = 'Btn'>
                <div className = 'Btn'>
                <button onClick = {handleClick}> First Choice</button>
                <button onClick = {handleClick}> Second Choice</button>
                <button onClick = {handleClick}> Third Choice</button>
                </div>
            </div>
        </div>
    )
}



        
import React from 'react'
import './Stats.css'
import Hearts from './Hearts.js'
export default function Stats() {
    const handleClick = () =>{
        console.log("Hello World");
    }
  return (
    <div className = 'Stats'>
        <h1 className ='card'> Banking For Good</h1>
        <Hearts hearts = {4} totHearts = {10}/>
        <button onClick = {handleClick}> First Choice</button>
        <button onClick = {handleClick}> Second Choice</button>
        <button onClick = {handleClick}> Third Choice</button>
        <div> Make a Decision</div>
    </div>
  )
}

import React from 'react'
import './Stats.css'
import Hearts from './Hearts.js'
import Balance from './Balance.js'
import Button from './Button.js'
export default function Stats() {
    
  return (
    <div className = 'Stats'>
        <h1 className ='card'> Banking For Good</h1>
        <Balance balance = {1000}/>
        <Hearts hearts = {4} totHearts = {10}/>
        <Button/>
        <div> Make a Decision</div>
    </div>
  )
}

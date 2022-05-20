import React from 'react'
import './Stats.css'
import Hearts from './Hearts.js'
import Balance from './Balance.js'
import Button from './Button.js'
import Interest from './Interest'


export default function Stats() {
    
  return (
    <div className = 'Stats'>
        <h1 className ='card'> Banking For Good</h1>
        <Balance balance = {1000}/>
        <Interest interest = {50}/>
        <Hearts hearts = {4} totHearts = {10}/>
        <div className = 'fourth'> Make a Decision</div>
        <Button/>
        <div className = 'card'>  1: Hello </div>
        <div className = 'card'>  2: Goodbye </div>
        <div className = 'card'>  3: Leave </div>
    </div>
  )
}

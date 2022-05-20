import React from 'react'
import './Stats.css'
import Hearts from './Hearts.js'
import Balance from './Balance.js'
import Interest from './Interest'
import Credit from './Credit'


export default function Stats3() {
    
  return (
    <div className = 'Stats'>
        <h1 className ='card'> Credit Journey</h1>
        <Balance balance = {300}/>
        <Interest interest = {15}/>
        <Credit credit = {200}/>
        <Hearts hearts = {7} totHearts = {10}/>
        <div className = 'fourth'> Make a Decision</div>
        
        <div className = 'card'>  1: You recieved a $500 bonus, do you spend it shopping?  </div>
        <div className = 'card'>  2: A new TV went on sale for $2000 do you buy it?</div>
        <div className = 'card'>  3: You recieved a new laptop, do you sell it for more money? </div>
    </div>
  )
}
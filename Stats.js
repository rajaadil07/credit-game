import React from 'react'
import './Stats.css'
import Hearts from './Hearts.js'
import Balance from './Balance.js'
import Interest from './Interest'
import Credit from './Credit'


export default function Stats0() {
    
  return (
    <div className = 'Stats'>
        <h1 className ='card'> Credit Journey</h1>
        <Balance balance = {1000}/>
        <Interest interest = {5}/>
        <Credit credit = {500}/>
        <Hearts hearts = {10} totHearts = {10}/>
        <div className = 'fourth'> Make a Decision</div>
        
        <div className = 'card'>  1: Your Car has broken down, do you spend money to fix it? </div>
        <div className = 'card'>  2: Your friends want to go out, do you spend money with them? </div>
        <div className = 'card'>  3: You car payment is due on tuesday, do you pay it late? </div>
    </div>
  )
}

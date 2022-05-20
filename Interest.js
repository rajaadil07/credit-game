import React from 'react'

export default function({amount}){
    return(
        <div style = {{"fontSize":15}}> 
            <div className = 'card'>
                <div className = 'third'>
                    Interest: {amount}
                </div>
            </div>
        </div>
    )
}
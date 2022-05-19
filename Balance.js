import React from 'react'

export default function({amount}){
    return(
        <div style = {{"fontSize":20}}> 
            <div className = 'card'>
                <div className = 'third'>
                    Balance: {amount}
                </div>
            </div>
        </div>
    )
}
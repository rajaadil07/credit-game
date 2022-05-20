import React from 'react'

export default function({balance}){
    return(
        <div style = {{"fontSize":15}}> 
            <div className = 'card'>
                <div className = 'third'>
                    Balance: {balance}
                </div>
            </div>
        </div>
    )
}
import React from 'react'

export default function({interest}){
    return(
        <div style = {{"fontSize":15}}> 
            <div className = 'card'>
                <div className = 'third'>
                    Interest: {interest}
                </div>
            </div>
        </div>
    )
}
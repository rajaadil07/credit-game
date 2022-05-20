import React from 'react'

export default function({credit}){
    return(
        <div style = {{"fontSize":15}}> 
            <div className = 'card'>
                <div className = 'third'>
                    Credit: {credit}
                </div>
            </div>
        </div>
    )
}
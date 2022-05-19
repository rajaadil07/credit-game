import React from 'react'

export default function({hearts,totHearts}){
    return(
        <div style = {{"fontSize":20}}> 
            <div className = 'card'>
                <h1 className = 'secondary'>
                    Health: {hearts}/{totHearts}
                </h1>
            </div>
        </div>
    )
}
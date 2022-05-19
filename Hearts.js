import React from 'react'

export default function({hearts,totHearts}){
    return(
        <div style = {{"fontSize":20}}> 
            <div className = 'card'>
                <div className = 'secondary'>
                    Health: {hearts}/{totHearts}
                </div>
            </div>
        </div>
    )
}
import React from 'react'
import Hearts from "./Hearts"
export default class Hud extends React.Component{

    state = {
        hearts: 3,
        totHearts: 10
    };
    render(){
        return(
            <div className = {"Hud"}>
                <Hearts hearts={this.state.hearts} totHearts={this.state.totHearts}/>
                <aside className = {"Sidebar"}>
                </aside>
            </div>
        )
    }
}
import React from 'react'
import Stats from './Stats.js'
import Stats0 from './Stats0.js'
import Stats2 from './Stats2.js'
import Stats3 from './Stats3.js'
import './App.css'
import {BrowserRouter as Router, Route, Switch,Routes,Link} from "react-router-dom";
import Button from './Button.js'
import Button2 from './Button2.js'
import Button3 from './Button3.js'

function App() {
  return (
    <>
    <Router>
    <nav>
      <div className = 'link'>
        <Link to = "/decision1"> <Button type = "button"/> </Link>
        <Link to = "/decision2"> <Button2 type = "button"/> </Link>
        <Link to = "/decision3"> <Button3 type = "button"/> </Link>
        </div>
      </nav>
      <Routes>
        <Route path = "/" element = {<h1 className ='App-header'> <Stats/> </h1>}/>

        <Route path = "/decision1" element = {<h1 className ='App-header'> <Stats0/> </h1>}/>

        <Route path = "/decision2" element = {<h1 className ='App-header'>  <Stats2/> </h1>}/> 

        <Route path = "/decision3" element = {<h1 className ='App-header'> <Stats3/> </h1>}/>          
      </Routes>
    </Router>
    </>
  )
}

export default App;

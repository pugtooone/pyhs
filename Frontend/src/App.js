import React, { Component } from "react";
import logo from "./logo.svg";
//Components
import Sidebar from "./Components/Sidebar.jsx"
//Stylesheet
import "./App.css";

import { eel } from "./eel.js";

class App extends Component {
  constructor(props) {
    super(props);
    eel.set_host("ws://localhost:8888");
    eel.hello();
  }
  
  
  render() {
    
    return (
      <>
      <Sidebar />
      <div className="MainPage"></div>
      </>
      
      
    );
  }
}

export default App;

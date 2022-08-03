import React, { Component } from "react";
import logo from "./logo.svg";
import Sidebar from "./Components/Sidebar.jsx"
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
      <Sidebar></Sidebar>
      
    );
  }
}

export default App;

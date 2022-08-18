import React, { Component ,useEffect} from "react";
//Components
import Sidebar from "./Components/Sidebar.jsx";
import MainPage from "./Pages/MainPage/MainPage.jsx";
//Stylesheet
import "./App.css";
//Eel
import { eel } from "./eel.js";

class App extends Component {
  constructor(props) {
    super(props);
    eel.set_host("ws://localhost:8888");
    eel.hello(); 
  }

//---------------------Render-------------------
  render() {

    return (
    <div>
      <Sidebar />
      <MainPage/>
    </div>
    );
  }
}

export default App;
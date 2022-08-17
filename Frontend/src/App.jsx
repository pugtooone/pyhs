import React, { Component, state } from "react";
//Components
import Sidebar from "./Components/Sidebar.jsx";
import Newfeed from "./Components/Main.Newfeed/Newfeed.jsx";
//Stylesheet
import "./App.css";
//Eel
import { eel } from "./eel.js";

class App extends Component {
  constructor(props) {
    super(props);
    eel.set_host("ws://localhost:8888");
    eel.hello();
    this.test = ["Kipling","OnTheList"];
    this.state = {brand:"Kipling",
                  jobnumber:"FW22 97",
                  date:"12/7"
                }
  }
  adder =() =>{
    console.log("clicked");
    this.setState({brand: "test"} )
  }

  getDate = () => {
    console.log("Get date");
    var date = new Date();
    date.getDate();
    console.log(date);
    return date;
  }

  render() {

    return (
      <>
      <Sidebar />
      <div className="MainPage">
        <div className="Hero">
        <div className="FeedsContainer">
          <div className="SendContainer" onClick={this.adder}>
            
          </div>
          <div className="QCContainer">
            <Newfeed date={this.state.date}>{this.state.brand + " " + this.state.jobnumber}</Newfeed>
          </div>
        </div>
        </div>
      </div>
      </>
    );
  }
}

export default App;
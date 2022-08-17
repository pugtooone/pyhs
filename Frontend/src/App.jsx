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
    this.state = {sendoutlist:[]
                };
    this.sendoutjoblist = [];
    //<Newfeed key="{item1}"date={this.state.date}>{this.state.jobname}</Newfeed>
  }

  checkjob =() =>{
    this.sendoutjoblist.push("Kipling FW22 97","OnTheList 123");
    console.log(this.sendoutjoblist);
    this.state.sendoutlist.push(this.sendoutjoblist.map((jobname) => <Newfeed>{jobname}</Newfeed>))
    console.log(this.state.sendoutlist)
    console.log("clicked");
  }



//---------------------Render-------------------

  render() {

    return (
      <>
      <Sidebar />
      <div className="MainPage">
        <div className="Hero">
        <div className="FeedsContainer">
          <div className="SendContainer" onClick={this.checkjob}>
            
          </div>
          <div className="QCContainer">
          </div>
        </div>
        </div>
      </div>
      </>
    );
  }
}

export default App;
import React, { Component } from 'react';
import "./MainPage.css";
import Newfeed from "../../Components/Main.Newfeed/Newfeed.jsx";


function MainPage() {
    const joblist = ["OnTheList"]
    const clickhandler = () =>{
        
    }

    return (
    <div className="MainPage">
        <div className="Hero">
            <div className="FeedsContainer">
                <div className="SendContainer">
                    {joblist.map((items)=><Newfeed>{items}</Newfeed>)}
                </div>
                <div className="QCContainer">
                    {joblist.map((items)=><Newfeed>{items}</Newfeed>)}
                </div>
            </div>
        </div>
    </div>



    )
}

export default MainPage;
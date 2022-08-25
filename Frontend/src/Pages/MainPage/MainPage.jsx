import React, { Component } from 'react';
import "./MainPage.css";
import Newfeed from "../../Components/Main.Newfeed/Newfeed.jsx";


function MainPage() {
    const joblist = ["OnTheList"];

    return (
    <div className="MainPage">
        <div className="Hero">
            <div className="FeedsContainer">
                
                <div className="SendContainer">
                    {joblist.map((items,key)=><Newfeed key = {key} date="12/5" action="QC">{items}</Newfeed>)}
                </div>
            </div>
        </div>
    </div>



    )
}

export default MainPage;

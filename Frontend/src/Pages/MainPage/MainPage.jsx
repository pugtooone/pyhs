import React, { Component } from 'react';
import "./MainPage.css";
import Newfeed from "../../Components/Main.Newfeed/Newfeed.jsx";


function MainPage() {
    const joblist = ["OnTheList","Kipling","Arena","Petit Bateau"]
    const clickhandler = () =>{
        
    }

    return (
    <div className="MainPage">
        <div className="Hero">
            <div className="FeedsContainer">
                <div className="SendContainer">
                    {joblist.map((items)=><Newfeed date="12/5">{items}</Newfeed>)}
                </div>
            </div>
        </div>
    </div>



    )
}

export default MainPage;
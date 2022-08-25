import React, { Component } from 'react';
import "./MainPage.css";
import Newfeed from "../../Components/Main.Newfeed/Newfeed.jsx";


function MainPage() {
    const joblist = [["OnTheList 102","QC"],"OnTheList 103","Kipling FW22 100","Kipling FW22 101","Arena","Petit Bateau"]
    const clickhandler = () =>{
        
    }

    return (
    <div className="MainPage">
        <div className="Hero">
            <div className="FeedsContainer">
                
                <div className="SendContainer">
                    {joblist.map((items,caction)=><Newfeed date="12/5" action={caction}>{items}</Newfeed>)}
                </div>
            </div>
        </div>
    </div>



    )
}

export default MainPage;
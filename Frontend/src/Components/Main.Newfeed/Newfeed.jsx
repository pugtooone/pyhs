import React, { Component, useState } from 'react';
import "./Newfeed.css";

function Newfeed(props){

    return(
    <div className ="Box">
        <div className="Circle"><box-icon name='file' color='#2B2A2E'></box-icon></div>
        <span className="Date">{props.date}</span>
        <span className="JobName">{props.children}</span>
        <div className ="Start">Start</div>
        <div className = "Snooze">Snooze</div>
        
        
    </div>
    );
}

export default Newfeed;

import React, { Component, useState } from 'react';
import "./Newfeed.css";

function Newfeed(props){

    return(
    <div className ="Box">
        <div className="Circle"><box-icon name='file' color='#2B2A2E'></box-icon></div>
        <span className="Date">12/5</span>
        <span className="JobName">{props.children}</span>
        
        
    </div>
    );
}

export default Newfeed;

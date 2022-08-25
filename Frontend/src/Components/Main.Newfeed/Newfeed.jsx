import React, { Component, useState } from 'react';
import "./Newfeed.css";

function Newfeed(props){
    //stylesheet

    const expandedcontent = {height:'100px',
                             display:'flex',
                             flexDirection:'column'
                            };
    //useState functions
    const [expand,setExpand] = useState(false);

    //Event Handler
    const expandhandler = () => {
        if (expand == false){
            setExpand(true);
        }
        else{
            setExpand(false);
        }
    
    }
    return(
    <div className ="Box" onClick={expandhandler} style={expand?{height:"100px"}:{height:"36px"}}>
        <div>
            <div className="Circle"><box-icon name='file' color='#2B2A2E'></box-icon></div>
            <span className="Date">{props.date}</span>
            <span className="JobName">{props.children}</span>
            <div className ="Start">Start</div>
            <div className = "Snooze">Snooze</div>
        </div>
    </div>
    );
}

export default Newfeed;

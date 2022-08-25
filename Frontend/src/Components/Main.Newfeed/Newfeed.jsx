import React, { Component, useState } from 'react';
import "./Newfeed.css";

function Newfeed(props){
    //stylesheet
    
    const expandedcontent = {height:'200px',
                             display:'flex',
                             flexDirection:'column',
                             transition:'height 2s ease-out'
                            };

    const unexpandcontent = {height:'36px',
                             transition:'height 0.5s'
                            };
    //useState functions
    const [expand,setExpand] = useState(false);
    const [urgent,setUrgent] = useState(false);

    //Event Handler

    const boxHandler = () => {
        expand?box_style.replace(expandedcontent):box_style.replace(unexpandcontent)
    };

    const expandhandler = () => {
        if (expand == false){
            setExpand(true);
        }
        else{
            setExpand(false);
        }
    };

    return(
    <div className ="Box" onClick={expandhandler} style={expand?expandedcontent:unexpandcontent}>
        <div onClick={boxHandler}>
            <div className="Circle"><box-icon name='file' color='#2B2A2E'></box-icon></div>
            <span className="Date">{props.date}</span>
            <span className="JobName">{props.children}</span>
            <div className ="Start">{props.action}</div>
            <div className = "Snooze">Snooze</div>
        </div>
        <div style={expand?{visibility:'visible',display:'relative',marginTop:'30px',opacity:'1',transition:'visibility 2s ease-out'}:{visibility:'hidden',opcaity:'0'}}>
            <span>Image Check List</span>
        </div>
    </div>
    );
}

export default Newfeed;

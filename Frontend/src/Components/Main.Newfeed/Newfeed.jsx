import React, { Component, useState } from 'react';
import "./Newfeed.css";

function Newfeed(props){
    //stylesheet
    
    const expandedcontent = {height:'200px',
                             transition:' height 0.5s ease-out, transform 0.4s',
                             
                            };

    const unexpandcontent = {height:'36px',
                             transition:' height 0.5s ease-out, transform 0.4s',
                             
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
    };

    return(
    <div className={props.urgent?'Urgent_Box':'Box'} style={expand?expandedcontent:unexpandcontent}>
        <div className='Surface'>
            <div className="Circle">
                <box-icon name='file' color='#2B2A2E'></box-icon>
            </div>
            <span className="Date">{props.date}</span>
            <span className="JobName" onClick={expandhandler}>{props.children}</span>
            <div className ="Start">Start</div>
            <div className = "Snooze">Snooze</div>
        </div>
        <div style={{marginTop:'30px'}}>
            <span>Vendor</span>
            <span>Dresma</span>
            
        </div>
    </div>
    );
}

export default Newfeed;

import React, { Component , props, useState } from 'react';
import './Mainfunction.css';




function Mainfunction(props){
    
    

    return(
    <div className='selector'>
        <a>
            <p>{props.children}</p>
            <div /*</a>className={noti?'circle':'circle-hidden'}*/></div>
        </a>
    </div>
    );
}

export default Mainfunction;



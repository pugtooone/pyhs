import React, { Component , props, useState } from 'react';
import './Mainfunction.css';

function Mainfunction(props){
const [noti,setNoti] = useState(false);

    return(
    <div className='selector'>
        <a href={String(props.link)}>
            <p>{String(props.type)}</p>
            <div className={noti?'circle':'circle-hidden'}></div>
        </a>
    </div>
    );
}

export default Mainfunction;



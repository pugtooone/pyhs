import React, { Component , props} from 'react';
import './Mainfunction.css';

function Mainfunction(props){

    return(
    <div className='selector'>
        <a href={String(props.link)}>
            <p>{String(props.type)}</p>
            <div className='circle'></div>
        </a>
    </div>
    );
}

export default Mainfunction;


/*<div className='Send'>
            <a href='#'><p>Send</p><div className='circle'></div></a>
          </div>*/
import React, { Component, props , useState} from 'react';
import './Statusbox.css';


function Statusbox(props){
    const [number,setNumber] = useState(1)
    const numcheck = () => {
        
        setNumber((number)=>number += 1)
    }




    return (
        <div className='Container' onClick={numcheck}>
            <div className='Status'>
                <div style={props.color}>{props.children}</div>
            </div>
            <div className="NumberContainer">
                {number}
            </div>
        </div>
    );
}

export default Statusbox;
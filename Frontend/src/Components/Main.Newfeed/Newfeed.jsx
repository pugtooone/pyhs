import React, { Component, useState } from 'react';
import "./Newfeed.css";

function Newfeed(){

    const [name,setName] = useState("SampleBrand 123");
    const brand = ["OnTheList","Kipling"]
    function changebrand(){
        setName(() => {return brand[1] + " 123";});
    }



    return(
    <div className ="Box" onClick={changebrand}>
        <div className="Circle"><box-icon name='file' color='#2B2A2E'></box-icon></div>
        <span className="Date">12/5</span>
        <span className="JobName">{name}</span>
        
        
    </div>
    );
}

export default Newfeed;
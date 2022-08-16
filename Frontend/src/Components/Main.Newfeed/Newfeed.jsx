import React, { Component, useState ,props} from 'react';
import "./Newfeed.css";

function Newfeed(props){

    const [name,setName] = useState("SampleBrand");
    const brand = ["OnTheList","Kipling"]
    
    const changejob = () => {
        name=="Kipling"?setName(()=> brand[0]):setName(() => brand[1]);
    }


    return(
    <div className ="Box" onClick={changejob}>
        <div className="Circle"><box-icon name='file' color='#2B2A2E'></box-icon></div>
        <span className="Date">12/5</span>
        <span className="JobName">{name}</span>
        
        
    </div>
    );
}

export default Newfeed;

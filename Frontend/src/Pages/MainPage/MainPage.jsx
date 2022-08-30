import React, { Component ,useState} from 'react';
import "./MainPage.css";
//Components
import Newfeed from "../../Components/Main.Newfeed/Newfeed.jsx";
import Statusbox from '../../Components/Main.Statusbox/Statusbox.jsx';
//eel
import { eel } from "../../eel";


function MainPage() {
    // Joblist Received -- Python functions
    const joblist = [{jobname:"OnTheList",date:"12/5",urgent:false},
                    {jobname:"Kipling",date:"13/5",urgent:false}
                    ];

    
    


    //useState Events
    const [qctype,setQctype] = useState(false);
    const [urgent,setUrgent] = useState(false);
    //useEffects function
    const urgentchecker = () => {
        return
    };

    //Render
    return (
    <div className="MainPage">
        <div className="Hero">
            <div className="StatusboxContainer">
            <Statusbox>Waiting QC</Statusbox>
            <Statusbox color={{background:'#ffff00'}}>Retouching</Statusbox>
            <Statusbox color={{background:'#432343'}}>Amending</Statusbox>
            </div>
            <div className="FeedsContainer">
                <div className="Type">
                    <div style={{color:'white'}}>Send<span className='break'/></div>
                    <div style={{color:'white'}}>QC</div>
                </div>
                <div className="SendContainer">
                    {joblist.map((item,index)=><Newfeed 
                                            key = {index}
                                            urgent ={item.urgent}
                                            date="12/5">
                                            {item.jobname}
                                            </Newfeed>)}
                </div>
            </div>
        </div>
    </div>

    )
}

export default MainPage;

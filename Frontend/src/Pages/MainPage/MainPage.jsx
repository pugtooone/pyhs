import React, { Component ,useState, useRef} from 'react';
import "./MainPage.css";
//Components
import Newfeed from "../../Components/Main.Newfeed/Newfeed.jsx";
import Statusbox from '../../Components/Main.Statusbox/Statusbox.jsx';
//eel
import { eel } from "../../eel";


function MainPage() {
    // Joblist Received -- Python functions
    const qcjoblist = [{jobname:"OnTheList",date:"12/5",urgent:false},
                    {jobname:"Kipling",date:"13/5",urgent:false}
                    ];

    const sendjoblist = [{jobname:"Petit Bateau 123",date:"12/5",urgent:false},
                    {jobname:"Kipling 123",date:"13/5",urgent:false}
                    ];

    // style

    //useState Events
    const [qctype,setQctype] = useState(false);
    const [urgent,setUrgent] = useState(false);
    //useEffects function
    
    
    //Render
    return (
    <div className="MainPage">
        <div className="Hero">
            <div className="StatusboxContainer">
            <Statusbox background={{background:'#000000'}}>Waiting QC</Statusbox>
            <Statusbox background={{background:'#f00f00'}}>Retouching</Statusbox>
            <Statusbox background={{background:'#432343'}}>Amending</Statusbox>
            </div>
            <div className="FeedsContainer">
                <div className="Type">
                    <div onClick={() => {qctype?setQctype(false):null}}>
                        Send
                    </div>
                    <div onClick={()=>{qctype?null:setQctype(true)}}>
                        QC
                    </div>
                </div>
                <span className={qctype?'QCState':'notQCState'}/>
                <div className="SendContainer">
                    {qctype?qcjoblist.map((item,index)=><Newfeed 
                                            style={{animation:'fadein',animationDuration:'1s',animationIterationCount:'1'}}
                                            key = {index}
                                            urgent ={item.urgent}
                                            date="12/5">
                                            {item.jobname}
                                            </Newfeed>)
                                            :
                                            sendjoblist.map((item,index)=><Newfeed 
                                            key = {index}
                                            urgent ={item.urgent}
                                            date="12/5">
                                            {item.jobname}
                                            </Newfeed>)
                                            }
                </div>
            </div>
        </div>
    </div>

    )
}

export default MainPage;

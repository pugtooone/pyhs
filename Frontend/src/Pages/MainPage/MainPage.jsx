import React, { Component ,useState} from 'react';
import "./MainPage.css";
import Newfeed from "../../Components/Main.Newfeed/Newfeed.jsx";


function MainPage() {
    // Joblist Received -- Python functions
    const joblist = [{jobname:"OnTheList",date:"12/5",urgent:true},
                    {jobname:"Kipling",date:"13/5",urgent:false}
                    ];

    //useState Events
    const [urgent,setUrgent] = useState(false);
    //useEffects function
    const urgentchecker = () => {
        return
    };

    //Render
    return (
    <div className="MainPage">
        <div className="Hero">
            <div className="FeedsContainer">
                
                <div className="SendContainer">
                    {joblist.map((item,key)=><Newfeed 
                                            id = {key} 
                                            urgent = {item.urgent}
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

import React,{ Component, useState } from 'react';
import 'boxicons'
import "./Sidebar.css";
import Mainfunction from './Sidebar.Mainfunction/Mainfunction.jsx';



function Sidebar() {
  
  const [alert, setAlertState] = useState(false);

  return (
    <div className='Mainbar'>
      <div className='items'>
        <div className='Home'>
          <box-icon color="white" name='home-alt-2'></box-icon>
        </div>
        <div className='Mainfunction'>
          <Mainfunction type="Send"></Mainfunction>
          <Mainfunction type="QC"></Mainfunction>
          <Mainfunction type="Submit"></Mainfunction>
        </div>
        <div className='Exit'>
          <box-icon color='white' animation='tada-hover' name='exit'></box-icon>
        </div>
      </div>
    </div>
  )
}



export default Sidebar;

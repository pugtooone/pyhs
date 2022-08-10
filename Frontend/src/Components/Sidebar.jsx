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
          <div className='QC'>
            <a href='#'><p>QC</p></a>
          </div>
          <div className='Submit'>
            <a href='#'><p>Submit</p></a>
          </div>
        </div>
        <div className='Exit'>
          <box-icon color='white' animation='tada-hover' name='exit'></box-icon>
        </div>
      </div>
    </div>
  )
}



export default Sidebar;

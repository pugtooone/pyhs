import React,{ Component, useState } from 'react';
import 'boxicons'
import "./Sidebar.css";



function Sidebar() {
  const [clickcount, setClickCount] = useState(0);

  return (
    <div className='Mainbar'>
      <div className='items'>
        <div className='Home'>
          <box-icon color="white" name='home-alt-2'></box-icon>
        </div>
        <div className='Mainfunction'>
          <div className='To Sent'>
            <a href='#'><p>Send</p></a>
          </div>
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

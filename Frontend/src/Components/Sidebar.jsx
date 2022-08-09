import React,{ Component, useState } from 'react';
import "./Sidebar.css";



function Sidebar() {
  const [clickcount, setClickCount] = useState(0);

  return (
    <div className='Mainbar'>
      <div className='items'>
        <div className='Home'>
          <p>Home</p>
        </div>
        <div className='Mainfunction'>
          <div className='To Sent'>
            <p>To Sent</p>
          </div>
          <div className='QC'>
            <a href='#'><p>QC</p></a>
          </div>
          <div className='Submit'>
            <a href='#'><p>Submit</p></a>
          </div>
        </div>
        <div className='Exit'>
          <p>Exit</p>
        </div>
      </div>
    </div>
  )
}



export default Sidebar;

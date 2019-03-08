import React, { Component } from 'react';
import './App.css';

function Textbox() {
    return (
      <div className="textbox-holder">
          <textarea className="textbox" placeholder="Enter text to be summarised here" rows="20" cols="70">
            
          </textarea>
      </div>
    );
}

export default Textbox;

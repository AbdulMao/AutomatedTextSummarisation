import React, { Component } from 'react';




function SummaryBox(props) {
  if(props.percentage==50){
    return (
      <div className="Summary-box">
            {props.summary.summary50}
            
      </div>
    );
  }
  else if(props.percentage==30){
    return (
      <div className="Summary-box">
            {props.summary.summary30}
            
      </div>
    );
  }
  else if(props.percentage==20){
    return (
      <div className="Summary-box">
            {props.summary.summary20}
            
      </div>
    );
  }
  else if(props.percentage==10){
    return (
      <div className="Summary-box">
            {props.summary.summary10}
            
      </div>
    );
  }
    
}

export default SummaryBox;

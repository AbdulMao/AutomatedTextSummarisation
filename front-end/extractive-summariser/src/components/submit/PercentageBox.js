import React, { Component } from 'react';

function PercentageDrop(){
    return (
        <div className= "Percentage-holder" id= "Percentage-holder">
            Choose summary size: &nbsp; 
            <select className= "Percentage-values">
                 <option value="50">50%</option>
                 <option value="30">30%</option>
                 <option value="20">20%</option>
                 <option value="10">10%</option>
            </select>
        </div>
    )
}


export default PercentageDrop;

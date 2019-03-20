import React, { Component } from 'react';
import { Link, withRouter} from "react-router-dom"
import makeSummaryRequest from './SummaryRequest.js';
import makeTopicRequest from './TopicRequest.js';

class SubmitButton extends Component {
  constructor(){
    super()  
  }
  onClick = () => {
    const mytext = document.querySelector(".textbox").value;
    var pValue = document.querySelector(".Percentage-values").value;
    this.props.history.push({
        pathname: '/summary',
        state: {
            myText: mytext,
            myPercentage: pValue
        }            
    })
}

  render(){
      return (
          <button onClick={this.onClick} className ="Submit-button" >
            Submit
          </button> 
      );
  }
}

export default withRouter(SubmitButton);
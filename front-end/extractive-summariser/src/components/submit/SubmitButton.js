import React, { Component } from 'react';
import { Link, withRouter} from "react-router-dom"
import makeSummaryRequest from './SummaryRequest.js';
import makeTopicRequest from './TopicRequest.js';
import PropTypes from 'prop-types';
import { hashHistory } from 'react-router-dom';


class SubmitButton extends Component {
  constructor(){
    super()  
  }
  onClick = () => {
    console.log("WE GOT THIS FAR")
    const mytext = document.querySelector(".textbox").value;
    console.log(mytext)
    this.props.history.push({
        pathname: '/summary',
        state: {
            myText: mytext
        }            
    })
    // const text = document.querySelector(".textbox").value;
    // var myJSON = {"text": text };
    // makeSummaryRequest(myJSON);
    // makeTopicRequest(myJSON);
    // console.log(myJSON)
    
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
import React, { Component } from 'react';
import TextBox from '../textBox/TextBox.js' 
import SubmitButton from '../submit/SubmitButton.js'
import makeSummaryRequest from '../submit/SummaryRequest.js';
import makeTopicRequest from '../submit/TopicRequest.js';


class HomePage extends Component {
    constructor(props){
      super(props)  
    }

    render(){
        return (
            <div className="App">
                <body className="App-header">
                    <TextBox />
                    <SubmitButton/>
                </body>
            </div>        
        );
    }
}

export default HomePage;
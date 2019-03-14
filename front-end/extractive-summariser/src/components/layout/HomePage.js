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
                    <div className="Logo-container"></div>
                    <div className="Info-container">INFO</div>
                    <div className="Input-container">
                        <TextBox />
                        {/* <select>
                            <option value="volvo">50%</option>
                            <option value="saab">30%</option>
                            <option value="opel">20%</option>
                            <option value="audi">10%</option>
                        </select> */}
                    </div>
                    <div className="Submit-container">
                        <SubmitButton/>
                    </div>                        
                </body>
            </div>        
        );
    }
}

export default HomePage;
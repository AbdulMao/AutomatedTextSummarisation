import React, { Component } from 'react';
import TextBox from '../textBox/TextBox.js' 
import SubmitButton from '../submit/SubmitButton.js'
import PercentageDrop from '../submit/PercentageBox.js';


class HomePage extends Component {
    constructor(props){
      super(props)  
    }

    render(){
        return (
            <div className="App">
                <body className="App-header">
                    <div className="Logo-container"></div>
                    <div className="Info-container">
                        Too Long; Didn't Read.
                        Quickly get the information you need, saving time! 
                    </div>
                    <PercentageDrop/>
                    <div className="Input-container">
                        <TextBox />
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
import React, { Component } from 'react';
import TextBox from '../textBox/TextBox.js' 
import SubmitButton from '../submit/SubmitButton.js'
import makeSummaryRequest from '../submit/SummaryRequest.js';
import makeTopicRequest from '../submit/TopicRequest.js';


class HomePage extends Component {
    constructor(props){
      super(props)  
    }

    // onClick = () => {
    //     console.log("WE GOT THIS FAR")
    //     const mytext = document.querySelector(".textbox").value;
    //     console.log(myText)
    //     this.props.history.push({
    //         pathname: '/template',
    //         state: {
    //             myText: mytext
    //         }
                
    //         })
    //     // const text = document.querySelector(".textbox").value;
    //     // var myJSON = {"text": text };
    //     // makeSummaryRequest(myJSON);
    //     // makeTopicRequest(myJSON);
    //     // console.log(myJSON)
        
    // }

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
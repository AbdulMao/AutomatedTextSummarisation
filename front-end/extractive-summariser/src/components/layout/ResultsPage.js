import React, { Component } from 'react';
import makeSummaryRequest from '../submit/SummaryRequest.js';
import makeTopicRequest from '../submit/TopicRequest.js';
import SummaryBox from '../results/SummaryBox.js'
import TopicBox from '../results/TopicBox.js'


class ResultsPage extends Component {
    constructor(){
      super()  
      this.state = {}
    }

    componentDidMount(){    
        const inputText = this.props.location.state.myText;
        var myJSON = {"text": inputText };
        makeTopicRequest(myJSON).then( (dataReturned) => {
            this.setState({
               myTopics: dataReturned.topics, 
            })
        })
        makeSummaryRequest(myJSON).then( (dataReturned) => {
            this.setState({
               mySummary: dataReturned, 
            })
        })
    

    }


    render(){
        if(!this.state.myTopics || !this.state.mySummary) return <p> loading </p>
        return (
            <div className="App">              
                <body className="App-header">
                    <div className="Logo-container"></div>
                    <div className="Info-container">Here is your Summary:</div>
                        <SummaryBox summary= {this.state.mySummary} percentage= {this.props.location.state.myPercentage} />
                        <TopicBox topics= {this.state.myTopics} />    
                </body>
            </div>   
              
        );
    }
    
}

export default ResultsPage;
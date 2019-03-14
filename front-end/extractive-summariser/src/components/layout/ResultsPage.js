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
               mySummary: dataReturned.summary, 
            })
        })
    

    }


    render(){
        console.log(this.state.myTopics)
        console.log("JIUA")
        if(!this.state.myTopics || !this.state.mySummary) return <p> loading </p>
        return (
            <div className="App">
                <body className="Results-page">
                    {/* <div>Results: {this.state.myTopics}</div>     
                    <div>summary: {this.state.mySummary}</div>   */}
                    <TopicBox topics= {this.state.myTopics} />
                    <SummaryBox summary= {this.state.mySummary} />

                </body>
            </div>   
              
        );
    }
    
}

export default ResultsPage;
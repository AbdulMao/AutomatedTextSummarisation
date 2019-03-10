import React, { Component } from 'react';


class ResultsPage extends Component {
    constructor(){
      super()  
    }

    render(){
        return (
            <div>Results: {this.props.location.state.myText}</div>       
        );
    }
    
}

export default ResultsPage;
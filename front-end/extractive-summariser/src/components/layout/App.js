import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from "react-router-dom"
// import logo from './logo.svg';
import './App.css';
import TextBox from '../textBox/TextBox.js' 
import SubmitButton from '../submit/SubmitButton.js'
import HomePage from './HomePage.js'
import ResultsPage from './ResultsPage.js'


class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route path="/" component={HomePage} exact />
          <Route path="/summary" component={ResultsPage}  />
        </Switch>   
      </BrowserRouter>
    );
  }
}

export default App;

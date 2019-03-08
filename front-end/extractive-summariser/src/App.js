import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import TextBox from './TextBox.js'
import SubmitButton from './SubmitButton.js'


class App extends Component {
  render() {
    return (
      <div className="App">
        <body className="App-header">
          {/* <img src={logo} className="App-logo" alt="logo" /> */}
          <TextBox />
          <SubmitButton />
        </body>
      </div>
    );
  }
}

export default App;

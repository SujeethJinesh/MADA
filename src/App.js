import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import FileUpload from './FileUpload.js';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div className="wrapper">
          <FileUpload/>
        </div>
      </div>
    );
  }
}

export default App;

import React, { Component } from 'react';
import '../static/css/App.css';
import FileUpload from './FileUpload.js';
import '../node_modules/muicss/dist/css/mui.css'; // need to maintain this for button styling >:(, TODO: fix this

class Main extends Component {

  render() {
    return (
      <div className="App">
        <header className="App-header">
          {/*<img src={Logo} className="App-logo" alt="logo" />*/}
          {/*<Logo/>*/}
        </header>
        <div className="wrapper">
          <FileUpload/>
        </div>
      </div>
    );
  }
}

export default Main;

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
          <div className="jumbotron text-center">
              <h1>
                  Many Algorithms for Data Analysis (MADA)
              </h1>
              <p className="lead">
                  This website is a tool for doing supervised learning. To use it, simply upload up to 1 mb of your data and its labels. You may also find it fit to preprocess your data a little bit before passing it here. However, I do basic preprocessing anyway on the back end so long as it is in the correct format.
              </p>
          </div>
        <div className="wrapper">
          <FileUpload/>
        </div>
      </div>
    );
  }
}

export default Main;

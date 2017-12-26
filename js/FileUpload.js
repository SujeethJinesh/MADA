import React, { Component } from 'react';
import Dropzone from 'react-dropzone';
import '../static/css/App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import FontIcon from 'material-ui/FontIcon';
import {blue500, red500, greenA200} from 'material-ui/styles/colors';

class FileUpload extends Component {
  constructor() {
    super();
    this.state = {
        data: [],
        labels: []
    }
  }

  onDropData(acceptedData, rejectedData) {
      if (acceptedData != null && acceptedData[0].size <= 500000) {
        this.setState({
            data: acceptedData
        });
      }
  }

  onDropLabels(acceptedLabels, rejectedLabels) {
    if (acceptedLabels != null && acceptedLabels[0].size <= 500000) {
        this.setState({
            labels: acceptedLabels
        });
    }
  }

  renderJSX(item) {
    return (
        <div>
            {item["f"].name}
            <MuiThemeProvider>
                <a href="#">
                <div>
                    <FontIcon
                      className="material-icons customstyle"
                      color={blue500}
                      styles={{ top:10,}}>clear
                      </FontIcon>
                </div>
                </a>
            </MuiThemeProvider>
        </div>
    );
  }

  render() {
    return (
      <section>
        <div className='rows'>
          <div>
            <Dropzone accept="text/plain, text/csv" onDrop={this.onDropData.bind(this)}>
              <p> Upload up to 1 mb of your training data (single file) </p>
            </Dropzone>
          </div>
          <div>
            <Dropzone accept="text/plain, text/csv" onDrop={this.onDropLabels.bind(this)}>
              <p> Upload up to 1 mb of your training labels </p>
            </Dropzone>
          </div>
        </div>
          <h2>Dropped files</h2>
          <p>Data</p>
            <ul>
             {
                this.state.data.map(f => <li key={f.name}>{this.renderJSX({f})}</li>)
             }
             </ul>
          <p>Labels</p>
          <ul>
            {
              this.state.labels.map(f => <li key={f.name}>{this.renderJSX({f})}</li>)
            }
          </ul>
      </section>
    );
  }
}

export default FileUpload;

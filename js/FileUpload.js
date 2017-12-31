import React, { Component } from 'react';
import Dropzone from 'react-dropzone';
import '../static/css/App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import FontIcon from 'material-ui/FontIcon';
import {blue500} from 'material-ui/styles/colors';
import {Button} from "muicss/react";
import axios from 'axios';

class FileUpload extends Component {
  constructor() {
    super();
    this.state = {
        data: [],
        labels: []
    };
    this.upload_data = this.upload_data.bind(this);
  }

  upload_data() {
      console.log("POST start");

      let formData = new FormData();

      let data = this.state.data[0];
      let labels = this.state.labels[0];

      formData.append("data", data);
      formData.append("labels", labels);

      axios.post('/upload_data', formData, {
          headers: {
              'Content-Type': 'multipart/form-data'
          }
      }).then(function (response) {
        console.log(response);
      }).catch(function (error) {
        console.log(error);
      });
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

  static renderJSX(item) {
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
                this.state.data.map(f => <li key={f.name}>{FileUpload.renderJSX({f})}</li>)
             }
             </ul>
          <p>Labels</p>
          <ul>
            {
              this.state.labels.map(f => <li key={f.name}>{FileUpload.renderJSX({f})}</li>)
            }
          </ul>
          <div>
          {/* TODO: Add functionality to button */}
            <Button variant='raised' color='primary' onClick={this.upload_data}>Submit</Button>
          </div>
      </section>
    );
  }
}

export default FileUpload;

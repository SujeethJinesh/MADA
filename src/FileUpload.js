import React, { Component } from 'react';
import Dropzone from 'react-dropzone';
import './App.css';

class FileUpload extends Component {
  constructor() {
    super()
    this.state = { data: [], labels: [] }
  }

  onDropData(data) {
    this.setState({
      data
    });
  }

  onDropLabels(labels) {
    this.setState({
      labels
    });
  }

  render() {
    return (
      <section>
        <div className='rows'>
          <div>
            {/* TODO: Decide if you should support multiple files */}
            <Dropzone onDrop={this.onDropData.bind(this)}>
              <p> Upload up to 1 mb of your training data (single file) </p>
            </Dropzone>
          </div>
          <div>
            <Dropzone onDrop={this.onDropLabels.bind(this)}>
              <p> Upload up to 1 mb of your training labels </p>
            </Dropzone>
          </div>
        </div>
        <aside>
          <h2>Dropped files</h2>
          <p>Data</p>
          <ul>
            {
              this.state.data.map(f => <li key={f.name}>{f.name} - {f.size} bytes</li>)
            }
          </ul>
          <p>Labels</p>
          <ul>
            {
              this.state.labels.map(f => <li key={f.name}>{f.name} - {f.size} bytes</li>)
            }
          </ul>
        </aside>
      </section>
    );
  }
}

export default FileUpload;

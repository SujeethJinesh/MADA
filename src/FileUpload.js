import React, { Component } from 'react';
import Dropzone from 'react-dropzone'
import './App.css'

class FileUpload extends Component {
  constructor() {
    super()
    this.state = { data: [], labels: [] }
  }

  onDrop(data) {
    this.setState({
      data
    });
  }

  render() {
    return (
      <section>
        <div className='rows'>
          <div>
            <Dropzone onDrop={this.onDrop.bind(this)}>
              <p> Upload up to 1 mb of your training data </p>
            </Dropzone>
          </div>
          <div>
            {/* TODO: Bind these two to their own state objects. I.e. Data and Labels */}
            <Dropzone onDrop={this.onDrop.bind(this)}>
              <p> Upload up to 1 mb of your training labels </p>
            </Dropzone>
          </div>
        </div>
        <aside>
          <h2>Dropped files</h2>
          <ul>
            {
              this.state.data.map(f => <li key={f.name}>{f.name} - {f.size} bytes</li>)
            }
          </ul>
        </aside>
      </section>
    );
  }
}

export default FileUpload;
